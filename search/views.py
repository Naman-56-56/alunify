from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from user.models import Alumni
from .models import SearchQuery

def search_alumni(request):
    """
    Advanced search function for finding alumni based on various criteria
    including batch (graduation year) and branch (department).
    """
    query = request.GET.get('q', '').strip()
    department = request.GET.get('department', '').strip()
    graduation_year = request.GET.get('graduation_year', '').strip()
    
    # Start with all alumni
    alumni_list = Alumni.objects.filter(is_alumni=True)
    
    # Apply filters based on user input
    if query:
        alumni_list = alumni_list.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query) |
            Q(email__icontains=query) |
            Q(company__icontains=query) |
            Q(current_position__icontains=query) |
            Q(location__icontains=query) |
            Q(bio__icontains=query)
        )
    
    if department:
        alumni_list = alumni_list.filter(department__iexact=department)
    
    # Handle graduation year filtering
    if graduation_year:
        # Check if it's a range (e.g., 2020-2025)
        if '-' in graduation_year:
            start_year, end_year = graduation_year.split('-')
            alumni_list = alumni_list.filter(
                graduation_year__gte=int(start_year),
                graduation_year__lte=int(end_year)
            )
        else:
            # It's a single year
            alumni_list = alumni_list.filter(graduation_year=int(graduation_year))
    
    # Store search query if any filters were applied
    if query or department or graduation_year:
        # Save the search query for analytics
        if request.user.is_authenticated:
            SearchQuery.objects.create(
                user=request.user,
                query=query,
                department=department,
                graduation_year=graduation_year
            )
        else:
            SearchQuery.objects.create(
                query=query,
                department=department,
                graduation_year=graduation_year
            )
    
    # Get unique graduation years and departments for filter dropdowns
    all_years = Alumni.objects.filter(is_alumni=True).values_list('graduation_year', flat=True).distinct().order_by('-graduation_year')
    all_departments = Alumni.objects.filter(is_alumni=True).values_list('department', flat=True).distinct().order_by('department')
    
    context = {
        'alumni_list': alumni_list,
        'query': query,
        'department': department,
        'graduation_year': graduation_year,
        'all_years': all_years,
        'all_departments': all_departments,
        'result_count': alumni_list.count()
    }
    
    return render(request, 'profiles/search_results.html', context)
