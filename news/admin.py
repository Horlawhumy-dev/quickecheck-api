from django.contrib import admin
from .models import HackerNewsID, QuickCheckItem, QuickCheckNews


class HackerNewsIDAdmin(admin.ModelAdmin):
    list_display = ('hackernews', 'fetched_at')
    list_display_links = ('hackernews', 'fetched_at')
    
admin.site.register(HackerNewsID, HackerNewsIDAdmin)

class QuickCheckItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'by')
    list_display_links = ('id',)
    
admin.site.register(QuickCheckItem, QuickCheckItemAdmin)

class QuickCheckNewsAdmin(admin.ModelAdmin):
    # list_display = ('title', 'type', 'by')
    # list_display_links = ('id',)
    
    admin.site.register(QuickCheckNews)