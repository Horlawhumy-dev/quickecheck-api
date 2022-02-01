from django.contrib import admin
from .models import News_ID


class NewsIdAdmin(admin.ModelAdmin):
    list_display = ('news', 'fetched_at')
    list_display_links = ('news', 'fetched_at')
    
admin.site.register(News_ID, NewsIdAdmin)