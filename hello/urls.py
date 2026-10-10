from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    # Home / Project
    path('', views.login_view, name='login'),
    path('project/', views.project_view, name='project'),

    # Adoption Categories
    path('dogs/', views.dogs_view, name='dogs'),
    path('cats/', views.cats_view, name='cats'),
    path('birds/', views.birds_view, name='birds'),
    path('others/', views.others_view, name='others'),

    # Medical Pages
    path('vaccination/', views.vaccinations_view, name='vaccination'),# This must match template link
    path('emergency/', views.emergency_view, name='emergency'),

    # Inspection
    path('inspection/', views.inspection_view, name='inspection'),

    # Legal Pages
    path('privacy/', views.privacy_view, name='privacy'),
    path('terms/', views.terms_view, name='terms'),
]
