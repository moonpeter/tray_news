from django.contrib import admin

# Register your models here.
from crawler.models import CrawlingData


class CrawlingDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'eng_title']
    list_display_links = ['id', 'eng_title']
    search_fields = ['eng_title']


admin.site.register(CrawlingData, CrawlingDataAdmin)
