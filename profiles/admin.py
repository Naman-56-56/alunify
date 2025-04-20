from django.contrib import admin
from .models import Experience, Education, Skill, AlumniSkill

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('alumni', 'title', 'company', 'start_date', 'end_date', 'is_current')
    list_filter = ('is_current', 'company')
    search_fields = ('title', 'company', 'alumni__first_name', 'alumni__last_name')

class EducationAdmin(admin.ModelAdmin):
    list_display = ('alumni', 'degree', 'institution', 'start_year', 'end_year', 'is_current')
    list_filter = ('institution', 'is_current')
    search_fields = ('degree', 'institution', 'alumni__first_name', 'alumni__last_name')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class AlumniSkillAdmin(admin.ModelAdmin):
    list_display = ('alumni', 'skill')
    list_filter = ('skill',)
    search_fields = ('alumni__first_name', 'alumni__last_name', 'skill__name')

admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(AlumniSkill, AlumniSkillAdmin)
