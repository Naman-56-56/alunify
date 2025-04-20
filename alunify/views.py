from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def profile(request):
    # Redirect to the new profiles app
    return redirect('profile_list')

def contribute(request):
    return render(request, 'contribute.html')

def connections(request):
    return render(request, 'connections.html')

def events(request):
    return render(request, 'events.html') 