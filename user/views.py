from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Alumni
from django.db import transaction

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_student:
                return redirect('student_dashboard')
            else:
                return redirect('alumni_dashboard')
        else:
            messages.error(request, 'Invalid email or password.')
    
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        try:
            with transaction.atomic():
                # Get form data
                full_name = request.POST.get('full_name')
                email = request.POST.get('email')
                password = request.POST.get('password')
                confirm_password = request.POST.get('confirm_password')
                department = request.POST.get('department')
                user_type = request.POST.get('user_type', 'alumni')  # Default to alumni if not specified
                
                # Get appropriate graduation year field based on user type
                if user_type == 'student':
                    graduation_year = request.POST.get('expected_graduation_year')
                    is_alumni = False
                    is_student = True
                else:
                    graduation_year = request.POST.get('graduation_year')
                    is_alumni = True
                    is_student = False

                # Validate passwords match
                if password != confirm_password:
                    messages.error(request, 'Passwords do not match.')
                    return redirect('register')

                # Create user
                user = Alumni.objects.create_user(
                    username=email,
                    email=email,
                    password=password,
                    first_name=full_name.split()[0],
                    last_name=' '.join(full_name.split()[1:]) if len(full_name.split()) > 1 else '',
                    graduation_year=graduation_year,
                    department=department,
                    is_alumni=is_alumni,
                    is_student=is_student
                )

                # Log the user in
                login(request, user)
                if is_student:
                    messages.success(request, 'Registration successful! Welcome to Student Connect.')
                    return redirect('student_dashboard')
                else:
                    messages.success(request, 'Registration successful! Welcome to Alumni Connect.')
                    return redirect('alumni_dashboard')

        except Exception as e:
            messages.error(request, f'Registration failed: {str(e)}')
            return redirect('register')

    return render(request, 'register.html')

@login_required
def alumni_dashboard(request):
    if not request.user.is_alumni:
        messages.error(request, 'Access denied. Alumni only area.')
        return redirect('login')
    return render(request, 'alumni_dashboard.html')

@login_required
def student_dashboard(request):
    if not request.user.is_student:
        messages.error(request, 'Access denied. Students only area.')
        return redirect('login')
    return render(request, 'student_dashboard.html')

def profile_view(request):
    # Redirect to the new profiles app
    return redirect('profile_list')

def connections_view(request):
    return render(request, 'connections.html')

def events_view(request):
    return render(request, 'events.html')

def contribute_view(request):
    return render(request, 'contribute.html')
