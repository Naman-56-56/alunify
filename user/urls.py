from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.alumni_dashboard, name='alumni_dashboard'),
    path('profile/', views.profile_view, name='profile'),
    path('connections/', views.connections_view, name='connections'),
    path('events/', views.events_view, name='events'),
    path('contribute/', views.contribute_view, name='contribute'),
] 