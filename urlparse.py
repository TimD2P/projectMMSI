import requests
from bs4 import BeautifulSoup
from time import sleep
#sleep (3) спим 3 секунды в цикле
mmsi=368054210
url = f'https://www.vesselfinder.com/vessels/details/{mmsi}'
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "lxml")

photourl = soup.find("img",class_="main-photo").get("src")

flag_1 = soup.find("table",class_="aparams")
flag_2 = flag_1.find("td",class_="n3", string='Flag')
flag_3= flag_2.find_next_sibling('td').text

print(photourl)
print(flag_3)