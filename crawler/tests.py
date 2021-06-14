from django.test import TestCase


# Create your tests here.
from crawler.models import CrawlingData


class SmokeTest(TestCase):
    def get_title_in_db(self):
        for i in CrawlingData.objects.all()[0:4:-1]:
            print(i)
        pass
