from django.contrib import admin
from .models import HackerNewsID, QuickCheckItem


class HackerNewsIDAdmin(admin.ModelAdmin):
    list_display = ('hackernews_id', 'fetched_at')
    list_display_links = ('hackernews_id', 'fetched_at')
    
admin.site.register(HackerNewsID, HackerNewsIDAdmin)

class QuickCheckItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'by')
    list_display_links = ('id',)
    
admin.site.register(QuickCheckItem, QuickCheckItemAdmin)