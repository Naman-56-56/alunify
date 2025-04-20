from django.contrib import admin
from .models import SearchQuery

class SearchQueryAdmin(admin.ModelAdmin):
    list_display = ('query', 'department', 'graduation_year', 'user', 'timestamp')
    list_filter = ('department', 'timestamp')
    search_fields = ('query', 'department', 'graduation_year', 'user__email', 'user__first_name', 'user__last_name')
    
admin.site.register(SearchQuery, SearchQueryAdmin)
