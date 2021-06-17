import requests
from bs4 import BeautifulSoup

webpage = requests.get("https://www.reuters.com/business/", verify=False)
soup = BeautifulSoup(webpage.content, "html.parser")

print(soup.findAll('div'))