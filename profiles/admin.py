from django.contrib import admin
from .models import Experience, Education, Skill, AlumniSkill, ProfessionCategory, AlumniProfession

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('alumni', 'title', 'company', 'start_date', 'end_date', 'is_current')
    list_filter = ('is_current', 'company')
    search_fields = ('title', 'company', 'alumni__first_name', 'alumni__last_name')

class EducationAdmin(admin.ModelAdmin):
    list_display = ('alumni', 'degree', 'institution', 'start_year', 'end_year', 'is_current')
    list_filter = ('institution', 'is_current')
    search_fields = ('degree', 'institution', 'alumni__first_name', 'alumni__last_name')

class ProfessionCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class AlumniProfessionAdmin(admin.ModelAdmin):
    list_display = ('alumni', 'category', 'specific_role', 'is_primary')
    list_filter = ('category', 'is_primary')
    search_fields = ('specific_role', 'alumni__first_name', 'alumni__last_name')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name',)

class AlumniSkillAdmin(admin.ModelAdmin):
    list_display = ('alumni', 'skill', 'proficiency_level')
    list_filter = ('skill', 'proficiency_level', 'skill__category')
    search_fields = ('alumni__first_name', 'alumni__last_name', 'skill__name')

admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(ProfessionCategory, ProfessionCategoryAdmin)
admin.site.register(AlumniProfession, AlumniProfessionAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(AlumniSkill, AlumniSkillAdmin)
