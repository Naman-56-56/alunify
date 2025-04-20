from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_list, name='profile_list'),
    path('my-profile/', views.my_profile, name='my_profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('add-experience/', views.add_experience, name='add_experience'),
    path('add-education/', views.add_education, name='add_education'),
    path('add-skill/', views.add_skill, name='add_skill'),
    path('remove-skill/<int:skill_id>/', views.remove_skill, name='remove_skill'),
    path('search/', views.search_alumni, name='search_alumni'),
    path('<int:alumni_id>/', views.profile_detail, name='profile_detail'),
] 