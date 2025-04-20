from django.contrib.auth.models import AbstractUser
from django.db import models

class Alumni(AbstractUser):
    email = models.EmailField(unique=True)
    graduation_year = models.IntegerField()
    department = models.CharField(max_length=50)
    is_alumni = models.BooleanField(default=True)
    is_student = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    current_position = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'graduation_year', 'department']

    def __str__(self):
        return f"{self.get_full_name()} ({self.email})"
