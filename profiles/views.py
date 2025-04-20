from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from user.models import Alumni
from .models import Experience, Education, Skill, AlumniSkill, ProfessionCategory, AlumniProfession
from django.db import models
from django.db.models import Count, Q, F, Case, When, Value, IntegerField
from django.db.utils import OperationalError, ProgrammingError

def profile_list(request):
    """Display a list of all alumni profiles with sorting options"""
    # Get sorting parameter
    sort_by = request.GET.get('sort', '-graduation_year')
    
    # Validate sort parameter
    valid_sort_fields = ['graduation_year', '-graduation_year', 'first_name', 'last_name', 
                         'department', 'current_position', 'company', 'location']
    if sort_by not in valid_sort_fields:
        sort_by = '-graduation_year'  # Default sort
    
    # Get filter parameters
    skill_filter = request.GET.get('skill', '')
    profession_filter = request.GET.get('profession', '')
    department_filter = request.GET.get('department', '')
    graduation_year_filter = request.GET.get('graduation_year', '')
    
    # Base queryset
    alumni_list = Alumni.objects.filter(is_alumni=True)
    
    # Apply filters - with error handling for missing tables
    try:
        if skill_filter:
            alumni_list = alumni_list.filter(alumni_skills__skill__name=skill_filter).distinct()
        
        if profession_filter:
            alumni_list = alumni_list.filter(
                Q(professions__category__name=profession_filter) | 
                Q(professions__specific_role__icontains=profession_filter)
            ).distinct()
    except (OperationalError, ProgrammingError):
        # Silently handle database errors if tables don't exist yet
        pass
    
    if department_filter:
        alumni_list = alumni_list.filter(department=department_filter)
    
    if graduation_year_filter:
        alumni_list = alumni_list.filter(graduation_year=graduation_year_filter)
    
    # Apply sorting
    alumni_list = alumni_list.order_by(sort_by)
    
    # Get filter options for dropdowns
    all_years = Alumni.objects.filter(is_alumni=True).values_list('graduation_year', flat=True).distinct().order_by('-graduation_year')
    all_departments = Alumni.objects.filter(is_alumni=True).values_list('department', flat=True).distinct().order_by('department')
    
    # Initialize variables with defaults in case of error
    all_skills = []
    all_professions = []
    
    # Try to get skills and professions, but handle errors if tables don't exist yet
    try:
        all_skills = Skill.objects.all().order_by('name')
        all_professions = ProfessionCategory.objects.all().order_by('name')
    except (OperationalError, ProgrammingError):
        # Database tables might not exist yet (migrations not applied)
        messages.warning(request, "Some features are not available yet. Please run migrations to enable all functionality.")
    
    context = {
        'alumni_list': alumni_list,
        'all_years': all_years,
        'all_departments': all_departments,
        'all_skills': all_skills,
        'all_professions': all_professions,
        'current_sort': sort_by,
        'skill_filter': skill_filter,
        'profession_filter': profession_filter,
        'department_filter': department_filter,
        'graduation_year_filter': graduation_year_filter,
    }
    
    return render(request, 'profiles/profile_list.html', context)

def profile_detail(request, alumni_id):
    """Display a specific alumni's profile details"""
    alumni = get_object_or_404(Alumni, id=alumni_id, is_alumni=True)
    experiences = Experience.objects.filter(alumni=alumni)
    educations = Education.objects.filter(alumni=alumni)
    
    # Initialize with defaults in case of error
    skills = []
    professions = []
    
    # Try to get skills and professions, but handle errors if tables don't exist yet
    try:
        skills = AlumniSkill.objects.filter(alumni=alumni).select_related('skill')
        professions = AlumniProfession.objects.filter(alumni=alumni).select_related('category')
    except (OperationalError, ProgrammingError):
        # Database tables might not exist yet (migrations not applied)
        pass
    
    context = {
        'alumni': alumni,
        'experiences': experiences,
        'educations': educations,
        'skills': skills,
        'professions': professions,
    }
    
    return render(request, 'profiles/profile_detail.html', context)

@login_required
def my_profile(request):
    """View the logged-in user's profile"""
    # Get the current user
    user = request.user
    
    # Handle both alumni and student profiles
    if user.is_student:
        # Student profile
        educations = Education.objects.filter(alumni=user)
        
        # Initialize with defaults in case of error
        skills = []
        
        # Try to get skills, but handle errors if tables don't exist yet
        try:
            skills = AlumniSkill.objects.filter(alumni=user).select_related('skill')
        except (OperationalError, ProgrammingError):
            # Database tables might not exist yet (migrations not applied)
            messages.warning(request, "Some features are not available yet. Please run migrations to enable all functionality.")
        
        context = {
            'alumni': user,  # We still use 'alumni' to maintain template compatibility
            'educations': educations,
            'skills': skills,
            'is_student': True
        }
        
        return render(request, 'profiles/my_profile.html', context)
    elif user.is_alumni:
        # Alumni profile (original code)
        experiences = Experience.objects.filter(alumni=user)
        educations = Education.objects.filter(alumni=user)
        
        # Initialize with defaults in case of error
        skills = []
        professions = []
        
        # Try to get skills and professions, but handle errors if tables don't exist yet
        try:
            skills = AlumniSkill.objects.filter(alumni=user).select_related('skill')
            professions = AlumniProfession.objects.filter(alumni=user).select_related('category')
        except (OperationalError, ProgrammingError):
            # Database tables might not exist yet (migrations not applied)
            messages.warning(request, "Some features are not available yet. Please run migrations to enable all functionality.")
        
        context = {
            'alumni': user,
            'experiences': experiences,
            'educations': educations,
            'skills': skills,
            'professions': professions,
            'is_student': False
        }
        
        return render(request, 'profiles/my_profile.html', context)
    else:
        messages.error(request, 'Access denied. Only registered users can access this page.')
        return redirect('index')

@login_required
def edit_profile(request):
    """Edit the logged-in user's basic profile information"""
    user = request.user
    
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.location = request.POST.get('location')
        user.bio = request.POST.get('bio')
        user.linkedin_url = request.POST.get('linkedin_url')
        user.twitter_url = request.POST.get('twitter_url')
        user.github_url = request.POST.get('github_url')
        
        # Handle specific fields based on user type
        if user.is_student:
            # For students, we store interests in the current_position field
            user.current_position = request.POST.get('interests')
            
            # Update expected graduation year if changed
            expected_graduation = request.POST.get('expected_graduation')
            if expected_graduation:
                user.graduation_year = expected_graduation
        else:
            # Alumni-specific fields
            user.current_position = request.POST.get('current_position')
            user.company = request.POST.get('company')
        
        if 'profile_picture' in request.FILES:
            user.profile_picture = request.FILES['profile_picture']
        
        user.save()
        messages.success(request, 'Profile updated successfully.')
        return redirect('my_profile')
    
    return render(request, 'profiles/edit_profile.html', {'alumni': user})

@login_required
def add_experience(request):
    """Add a new work experience to the profile"""
    if not request.user.is_alumni:
        messages.error(request, 'Only alumni can access this page.')
        return redirect('index')
    
    if request.method == 'POST':
        title = request.POST.get('title')
        company = request.POST.get('company')
        start_date = request.POST.get('start_date')
        is_current = 'is_current' in request.POST
        end_date = None if is_current else request.POST.get('end_date')
        description = request.POST.get('description')
        
        Experience.objects.create(
            alumni=request.user,
            title=title,
            company=company,
            start_date=start_date,
            end_date=end_date,
            is_current=is_current,
            description=description
        )
        
        messages.success(request, 'Experience added successfully.')
        return redirect('my_profile')
    
    return render(request, 'profiles/add_experience.html')

@login_required
def add_education(request):
    """Add a new education entry to the profile"""
    if not request.user.is_alumni:
        messages.error(request, 'Only alumni can access this page.')
        return redirect('index')
    
    if request.method == 'POST':
        degree = request.POST.get('degree')
        institution = request.POST.get('institution')
        start_year = request.POST.get('start_year')
        is_current = 'is_current' in request.POST
        end_year = None if is_current else request.POST.get('end_year')
        description = request.POST.get('description')
        
        Education.objects.create(
            alumni=request.user,
            degree=degree,
            institution=institution,
            start_year=start_year,
            end_year=end_year,
            is_current=is_current,
            description=description
        )
        
        messages.success(request, 'Education added successfully.')
        return redirect('my_profile')
    
    return render(request, 'profiles/add_education.html')

@login_required
def add_profession(request):
    """Add a profession to the alumni profile"""
    if not request.user.is_alumni:
        messages.error(request, 'Only alumni can access this page.')
        return redirect('index')
    
    # Check if the necessary tables exist
    try:
        ProfessionCategory.objects.count()
    except (OperationalError, ProgrammingError):
        messages.error(request, "This feature is not available yet. Please run database migrations to enable it.")
        return redirect('my_profile')
    
    if request.method == 'POST':
        category_id = request.POST.get('category')
        specific_role = request.POST.get('specific_role')
        is_primary = 'is_primary' in request.POST
        
        # If marked as primary, unmark any current primary profession
        if is_primary:
            AlumniProfession.objects.filter(alumni=request.user, is_primary=True).update(is_primary=False)
        
        AlumniProfession.objects.create(
            alumni=request.user,
            category_id=category_id,
            specific_role=specific_role,
            is_primary=is_primary
        )
        
        messages.success(request, 'Profession added successfully.')
        return redirect('my_profile')
    
    categories = ProfessionCategory.objects.all().order_by('name')
    return render(request, 'profiles/add_profession.html', {'categories': categories})

@login_required
def remove_profession(request, profession_id):
    """Remove a profession from the profile"""
    if not request.user.is_alumni:
        messages.error(request, 'Only alumni can access this page.')
        return redirect('index')
    
    try:
        profession = get_object_or_404(AlumniProfession, id=profession_id, alumni=request.user)
        profession.delete()
        messages.success(request, 'Profession removed successfully.')
    except (OperationalError, ProgrammingError):
        messages.error(request, "This feature is not available yet. Please run database migrations to enable it.")
    
    return redirect('my_profile')

@login_required
def add_skill(request):
    """Add skills to the profile with proficiency level"""
    if not request.user.is_alumni:
        messages.error(request, 'Only alumni can access this page.')
        return redirect('index')
    
    # Check if the necessary tables exist
    try:
        Skill.objects.count()
    except (OperationalError, ProgrammingError):
        messages.error(request, "This feature is not available yet. Please run database migrations to enable it.")
        return redirect('my_profile')
    
    if request.method == 'POST':
        skill_id = request.POST.get('skill')
        proficiency = request.POST.get('proficiency_level', 3)
        
        # If skill selected from dropdown
        if skill_id:
            # Add to the alumni's skills or update proficiency if already present
            alumni_skill, created = AlumniSkill.objects.update_or_create(
                alumni=request.user, 
                skill_id=skill_id,
                defaults={'proficiency_level': proficiency}
            )
        else:
            # Get or create skills by name
            skill_names = request.POST.get('skill_names', '').split(',')
            for name in skill_names:
                name = name.strip()
                if name:
                    # Get or create the skill
                    skill, created = Skill.objects.get_or_create(name=name)
                    
                    # Add to the alumni's skills if not already present, or update proficiency
                    alumni_skill, created = AlumniSkill.objects.update_or_create(
                        alumni=request.user, 
                        skill=skill,
                        defaults={'proficiency_level': proficiency}
                    )
        
        messages.success(request, 'Skills added successfully.')
        return redirect('my_profile')
    
    skills = Skill.objects.all().order_by('name')
    return render(request, 'profiles/add_skill.html', {'skills': skills})

@login_required
def remove_skill(request, skill_id):
    """Remove a skill from the profile"""
    if not request.user.is_alumni:
        messages.error(request, 'Only alumni can access this page.')
        return redirect('index')
    
    try:
        alumni_skill = get_object_or_404(AlumniSkill, alumni=request.user, skill_id=skill_id)
        alumni_skill.delete()
        messages.success(request, 'Skill removed successfully.')
    except (OperationalError, ProgrammingError):
        messages.error(request, "This feature is not available yet. Please run database migrations to enable it.")
    
    return redirect('my_profile')

def search_alumni(request):
    """Advanced search for alumni based on multiple criteria"""
    query = request.GET.get('q', '')
    department = request.GET.get('department', '')
    graduation_year = request.GET.get('graduation_year', '')
    skill = request.GET.get('skill', '')
    profession = request.GET.get('profession', '')
    location = request.GET.get('location', '')
    sort_by = request.GET.get('sort', '-graduation_year')
    
    # Validate sort parameter
    valid_sort_fields = ['graduation_year', '-graduation_year', 'first_name', 'last_name', 
                         'department', 'current_position', 'company', 'location']
    if sort_by not in valid_sort_fields:
        sort_by = '-graduation_year'  # Default sort
    
    # Base queryset
    alumni_list = Alumni.objects.filter(is_alumni=True)
    
    # Apply filters
    if query:
        alumni_list = alumni_list.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query) |
            Q(company__icontains=query) |
            Q(current_position__icontains=query) |
            Q(location__icontains=query) |
            Q(bio__icontains=query)
        )
    
    if department:
        alumni_list = alumni_list.filter(department=department)
    
    if graduation_year:
        alumni_list = alumni_list.filter(graduation_year=graduation_year)
    
    # Apply skill and profession filters with error handling
    try:
        if skill:
            alumni_list = alumni_list.filter(alumni_skills__skill__name=skill).distinct()
        
        if profession:
            alumni_list = alumni_list.filter(
                Q(professions__category__name=profession) | 
                Q(professions__specific_role__icontains=profession)
            ).distinct()
    except (OperationalError, ProgrammingError):
        # Silently handle database errors if tables don't exist yet
        pass
    
    if location:
        alumni_list = alumni_list.filter(location__icontains=location)
    
    # Apply sorting
    alumni_list = alumni_list.order_by(sort_by)
    
    # Get filter options for dropdowns
    all_years = Alumni.objects.filter(is_alumni=True).values_list('graduation_year', flat=True).distinct().order_by('-graduation_year')
    all_departments = Alumni.objects.filter(is_alumni=True).values_list('department', flat=True).distinct().order_by('department')
    
    # Initialize variables with defaults in case of error
    all_skills = []
    all_professions = []
    
    # Try to get skills and professions, but handle errors if tables don't exist yet
    try:
        all_skills = Skill.objects.all().order_by('name')
        all_professions = ProfessionCategory.objects.all().order_by('name')
    except (OperationalError, ProgrammingError):
        # Database tables might not exist yet (migrations not applied)
        messages.warning(request, "Some features are not available yet. Please run migrations to enable all functionality.")
    
    return render(request, 'profiles/search_results.html', {
        'alumni_list': alumni_list,
        'query': query,
        'department': department,
        'graduation_year': graduation_year,
        'skill': skill,
        'profession': profession,
        'location': location,
        'current_sort': sort_by,
        'all_years': all_years,
        'all_departments': all_departments,
        'all_skills': all_skills,
        'all_professions': all_professions
    })
