from django.db import models
from user.models import Alumni

class Experience(models.Model):
    alumni = models.ForeignKey(Alumni, on_delete=models.CASCADE, related_name='experiences')
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.title} at {self.company}"

class Education(models.Model):
    alumni = models.ForeignKey(Alumni, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-end_year']
        verbose_name_plural = 'Education'
    
    def __str__(self):
        return f"{self.degree} from {self.institution}"

class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class AlumniSkill(models.Model):
    alumni = models.ForeignKey(Alumni, on_delete=models.CASCADE, related_name='alumni_skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('alumni', 'skill')
        
    def __str__(self):
        return f"{self.alumni.get_full_name()} - {self.skill.name}"
