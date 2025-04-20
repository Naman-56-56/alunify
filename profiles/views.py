from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from user.models import Alumni
from .models import Experience, Education, Skill, AlumniSkill
from django.db import models

def profile_list(request):
    """Display a list of all alumni profiles"""
    alumni_list = Alumni.objects.filter(is_alumni=True).order_by('-graduation_year')
    return render(request, 'profiles/profile_list.html', {'alumni_list': alumni_list})

def profile_detail(request, alumni_id):
    """Display a specific alumni's profile details"""
    alumni = get_object_or_404(Alumni, id=alumni_id, is_alumni=True)
    experiences = Experience.objects.filter(alumni=alumni)
    educations = Education.objects.filter(alumni=alumni)
    skills = Skill.objects.filter(alumniskill__alumni=alumni)
    
    context = {
        'alumni': alumni,
        'experiences': experiences,
        'educations': educations,
        'skills': skills,
    }
    
    return render(request, 'profiles/profile_detail.html', context)

@login_required
def my_profile(request):
    """View the logged-in user's profile"""
    if not request.user.is_alumni:
        messages.error(request, 'Only alumni can access this page.')
        return redirect('index')
    
    alumni = request.user
    experiences = Experience.objects.filter(alumni=alumni)
    educations = Education.objects.filter(alumni=alumni)
    skills = Skill.objects.filter(alumniskill__alumni=alumni)
    
    context = {
        'alumni': alumni,
        'experiences': experiences,
        'educations': educations,
        'skills': skills,
    }
    
    return render(request, 'profiles/my_profile.html', context)

@login_required
def edit_profile(request):
    """Edit the logged-in user's basic profile information"""
    if not request.user.is_alumni:
        messages.error(request, 'Only alumni can access this page.')
        return redirect('index')
    
    if request.method == 'POST':
        alumni = request.user
        alumni.first_name = request.POST.get('first_name')
        alumni.last_name = request.POST.get('last_name')
        alumni.location = request.POST.get('location')
        alumni.current_position = request.POST.get('current_position')
        alumni.company = request.POST.get('company')
        alumni.bio = request.POST.get('bio')
        alumni.linkedin_url = request.POST.get('linkedin_url')
        alumni.twitter_url = request.POST.get('twitter_url')
        alumni.github_url = request.POST.get('github_url')
        
        if 'profile_picture' in request.FILES:
            alumni.profile_picture = request.FILES['profile_picture']
        
        alumni.save()
        messages.success(request, 'Profile updated successfully.')
        return redirect('my_profile')
    
    return render(request, 'profiles/edit_profile.html', {'alumni': request.user})

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
def add_skill(request):
    """Add skills to the profile"""
    if not request.user.is_alumni:
        messages.error(request, 'Only alumni can access this page.')
        return redirect('index')
    
    if request.method == 'POST':
        skill_names = request.POST.get('skills').split(',')
        
        for name in skill_names:
            name = name.strip()
            if name:
                # Get or create the skill
                skill, created = Skill.objects.get_or_create(name=name)
                
                # Add to the alumni's skills if not already present
                AlumniSkill.objects.get_or_create(alumni=request.user, skill=skill)
        
        messages.success(request, 'Skills added successfully.')
        return redirect('my_profile')
    
    return render(request, 'profiles/add_skill.html')

@login_required
def remove_skill(request, skill_id):
    """Remove a skill from the profile"""
    if not request.user.is_alumni:
        messages.error(request, 'Only alumni can access this page.')
        return redirect('index')
    
    alumni_skill = get_object_or_404(AlumniSkill, alumni=request.user, skill_id=skill_id)
    alumni_skill.delete()
    
    messages.success(request, 'Skill removed successfully.')
    return redirect('my_profile')

def search_alumni(request):
    """Search for alumni based on various criteria"""
    query = request.GET.get('q', '')
    department = request.GET.get('department', '')
    graduation_year = request.GET.get('graduation_year', '')
    
    alumni_list = Alumni.objects.filter(is_alumni=True)
    
    if query:
        alumni_list = alumni_list.filter(
            models.Q(first_name__icontains=query) | 
            models.Q(last_name__icontains=query) |
            models.Q(company__icontains=query) |
            models.Q(current_position__icontains=query) |
            models.Q(location__icontains=query)
        )
    
    if department:
        alumni_list = alumni_list.filter(department=department)
    
    if graduation_year:
        alumni_list = alumni_list.filter(graduation_year=graduation_year)
    
    return render(request, 'profiles/search_results.html', {
        'alumni_list': alumni_list,
        'query': query,
        'department': department,
        'graduation_year': graduation_year
    })
