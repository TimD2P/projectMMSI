import requests
from bs4 import BeautifulSoup
from time import sleep

#sleep (3) спим 3 секунды в цикле
mmsi=503000101
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0"}
response = requests.get(url=f'https://www.vesselfinder.com/vessels/details/{mmsi}', headers=headers)
soup = BeautifulSoup(response.text, features="lxml")
try:
    photourl = soup.find(name="img",class_="main-photo").get("src")
    flag_1 = soup.find(name="table",class_="aparams")
    flag_2 = flag_1.find("td",class_="n3", string='Flag')
    country = flag_2.find_next_sibling('td').text
    print(photourl)
    print(country)
except:
    pass
    photourl = 'https://tepeseo.com/wp-content/uploads/2019/05/404notfound.png'
    country = 'Not Found'
    print(photourl)
    print(country)