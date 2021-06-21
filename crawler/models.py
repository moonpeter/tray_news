from datetime import datetime

from django.db import models


class CrawlingData(models.Model):
    news_site = models.CharField(max_length=50, default='')
    post_date = models.DateTimeField(default=datetime.now)
    eng_title = models.CharField(max_length=200, default='')
    eng_sub_title = models.CharField(max_length=200, default='')
    eng_content = models.TextField(default='')
    ko_title = models.CharField(max_length=200, default='')
    ko_sub_title = models.CharField(max_length=200, default='')
    ko_content = models.TextField(default='')