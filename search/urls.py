from django.urls import path
from . import views

urlpatterns = [
    path('alumni/', views.search_alumni, name='search_alumni'),
] 