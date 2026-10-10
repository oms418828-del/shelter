from django.shortcuts import render

# Home / Project Page
def project_view(request):
    return render(request, 'project.html')

# Login Page
def login_view(request):
    return render(request, 'login.html')

# Adoption Categories
def dogs_view(request):
    return render(request, 'dogs.html')

def cats_view(request):
    return render(request, 'cats.html')

def birds_view(request):
    return render(request, 'birds.html')

def others_view(request):
    return render(request, 'others.html')

# Medical Pages
def vaccinations_view(request):
    return render(request, 'hello/vaccinations.html')

def emergency_view(request):
    return render(request, 'emergency.html')

# Inspection
def inspection_view(request):
    return render(request, 'inspection.html')

# Legal Pages
def privacy_view(request):
    return render(request, 'privacy.html')

def terms_view(request):
    return render(request, 'terms.html')
