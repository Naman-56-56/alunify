from django.db import models
from user.models import Alumni

# Create your models here.

class SearchQuery(models.Model):
    """Model to store user search queries for analytics"""
    user = models.ForeignKey(Alumni, on_delete=models.CASCADE, null=True, blank=True)
    query = models.CharField(max_length=255)
    department = models.CharField(max_length=100, blank=True)
    graduation_year = models.CharField(max_length=10, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Search queries'
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.query} ({self.timestamp.strftime('%Y-%m-%d %H:%M')})"
