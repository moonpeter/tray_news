from django.contrib import admin

# Register your models here.
from crawler.models import CrawlingData


class CrawlingDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'news_site', 'eng_title']
    list_display_links = ['id', 'news_site', 'eng_title']
    search_fields = ['eng_title', 'news_site']


admin.site.register(CrawlingData, CrawlingDataAdmin)
