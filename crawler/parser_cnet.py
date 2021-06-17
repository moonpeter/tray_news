import datetime
import os

import requests
from bs4 import BeautifulSoup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django

django.setup()

import urllib3
# InsecureRequestWarning 제거
urllib3.disable_warnings()

from crawler.models import CrawlingData


def get_list():
    print(" ========== start crawling ========== ")
    webpage = requests.get("https://www.cnet.com/news/", verify=False)
    soup = BeautifulSoup(webpage.content, "html.parser")

    the_latest = soup.find("div", {"class": "col-8 fdListing"})
    cnet_title = the_latest.findAll(attrs={'class': 'assetHed'})

    if len(CrawlingData.objects.all()) > 0:
        get_title_in_db()

    for i in range(10, 0, -2):
        title = cnet_title[i].text.strip()

        content_page = "https://www.cnet.com" + cnet_title[i]['href']
        soup_content = BeautifulSoup(requests.get(content_page).content, "html.parser")
        content_in_p = soup_content.findAll("p")
        sub_title = content_in_p[0].text.strip()

        main_content = ''

        for j in range(1, len(content_in_p)):
            if content_in_p[j].parent.parent.name == "figcaption":
                continue
            try:
                if content_in_p[j].attrs['class'][0] == "description":
                    continue
            except KeyError:
                pass
            main_content += content_in_p[j].text

        if title not in title_list_in_db:
            crawling_data = CrawlingData(
                news_site='Cnet',
                eng_title=title,
                eng_sub_title=sub_title,
                eng_content=main_content,
            )
            crawling_data.save()
    print("get_list() === time : ", datetime.datetime.now())
    print(" ========== finished crawling ========== ")
    return title_list_in_db.clear()


title_list_in_db = []


# DB에서 최신 5개의 제목 정보를 가져오는 메서드
def get_title_in_db():
    for i in range(0, 5):
        title_list_in_db.append(CrawlingData.objects.all().order_by('-id').values('eng_title')[i]['eng_title'])
    print("CrawlingData의 갯수 ? ", len(CrawlingData.objects.all()))
    print("title_list_in_db : ", title_list_in_db)
    return title_list_in_db


get_list()
