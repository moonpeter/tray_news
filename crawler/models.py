from django.db import models


class CrawlingData(models.Model):
    news_site = models.CharField(max_length=30, blank=True)
    eng_title = models.CharField(max_length=200, blank=True)
    eng_sub_title = models.CharField(max_length=200, blank=True)
    eng_content = models.TextField(blank=True)
    ko_title = models.CharField(max_length=200, blank=True)
    ko_sub_title = models.CharField(max_length=200, blank=True)
    ko_content = models.TextField(blank=True)
