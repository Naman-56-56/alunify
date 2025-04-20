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

# Define profession categories for better organization
class ProfessionCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = 'Profession Categories'
    
    def __str__(self):
        return self.name

# Add profession to Alumni model via a related field
class AlumniProfession(models.Model):
    alumni = models.ForeignKey(Alumni, on_delete=models.CASCADE, related_name='professions')
    category = models.ForeignKey(ProfessionCategory, on_delete=models.CASCADE)
    specific_role = models.CharField(max_length=100)
    is_primary = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('alumni', 'category', 'specific_role')
        
    def __str__(self):
        return f"{self.alumni.get_full_name()} - {self.specific_role} ({self.category.name})"

class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=50, blank=True, null=True, 
                               choices=[
                                   ('technical', 'Technical Skill'),
                                   ('soft', 'Soft Skill'),
                                   ('language', 'Language'),
                                   ('certification', 'Certification'),
                                   ('other', 'Other')
                               ])
    
    def __str__(self):
        return self.name

class AlumniSkill(models.Model):
    alumni = models.ForeignKey(Alumni, on_delete=models.CASCADE, related_name='alumni_skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    proficiency_level = models.IntegerField(default=3, choices=[
        (1, 'Beginner'),
        (2, 'Intermediate'),
        (3, 'Advanced'),
        (4, 'Expert'),
        (5, 'Master')
    ])
    
    class Meta:
        unique_together = ('alumni', 'skill')
        
    def __str__(self):
        return f"{self.alumni.get_full_name()} - {self.skill.name}"
