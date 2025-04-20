from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Alumni

class AlumniAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'graduation_year', 'department', 'is_alumni', 'is_student')
    search_fields = ('email', 'first_name', 'last_name', 'department')
    ordering = ('email',)
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'graduation_year', 'department')}),
        ('Status', {'fields': ('is_alumni', 'is_student')}),
        ('Profile', {'fields': ('profile_picture', 'bio', 'current_position', 'company', 'location')}),
        ('Social Links', {'fields': ('linkedin_url', 'twitter_url', 'github_url')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'graduation_year', 'department'),
        }),
    )

admin.site.register(Alumni, AlumniAdmin)
