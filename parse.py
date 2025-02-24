import pandas as pd
import psycopg2
import re
import requests
from bs4 import BeautifulSoup
from time import sleep


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0"}

pattern = r'[^\w\s]'

host = "localhost"
port = 8000
dbname = "postgres"
user = "postgres"
password = "Son40788"

sheet = pd.read_csv("AISsmalltest.csv")
sheet = sheet.fillna(0)

sheet["BaseDateTime"] = pd.to_datetime(sheet["BaseDateTime"])
#sheet.info(verbose=True, show_counts=True)
#sheet.head()
sheet_sorted = sheet.sort_values(by=["BaseDateTime"])
sheet_result = sheet_sorted.groupby(["MMSI", sheet_sorted["BaseDateTime"].dt.floor("h")], as_index=False).first()
#sheet_result.info()
#sheet_result.head()

sheet_for_map = sheet_result.drop(['SOG', 'COG', 'Heading', 'VesselName', 'IMO', 'CallSign', 'VesselType', 'Status', 'Length', 'Width', 'Draft', 'Cargo', 'TransceiverClass'], axis=1)
sheet_for_map = sheet_for_map.reindex(columns=['MMSI', 'LAT', 'LON', 'BaseDateTime'])
sheet_for_map.info(verbose=True, show_counts=True)
sheet_for_map.head()

sheet_for_info = sheet_result.drop(['BaseDateTime', 'LAT', 'LON', 'Heading', 'IMO', 'CallSign', 'Status', 'TransceiverClass'], axis=1).drop_duplicates(subset=["MMSI"], keep="first")
sheet_for_info = sheet_for_info.reindex(columns=['MMSI', 'VesselName', 'VesselType', 'Cargo', 'SOG', 'COG', 'Length', 'Width', 'Draft'])
sheet_for_info.info(verbose=True, show_counts=True)
sheet_for_info.head()

try:
    connection = psycopg2.connect(host=host, port=port, database=dbname, user=user, password=password)
    connection.autocommit = True
    for stroka_info in sheet_for_info.itertuples():
        sleep(5)
        response = requests.get(url=f'https://www.vesselfinder.com/vessels/details/{stroka_info[1]}', headers=headers)
        soup = BeautifulSoup(response.text, features="lxml")
        try:
            flag_1 = soup.find(name="table", class_="aparams")
            flag_2 = flag_1.find("td", class_="n3", string='Flag')
            country = flag_2.find_next_sibling('td').text
            photourl = soup.find(name="img", class_="main-photo").get("src")
        except:
            pass
            photourl = 'https://tepeseo.com/wp-content/uploads/2019/05/404notfound.png'
            country = 'Not Found'
        with connection.cursor() as cursor:
            ship_name = f'{stroka_info[2]}'
            ship_name = re.sub(pattern, '',ship_name)
            cursor.execute(f"insert into vesselinfo VALUES({stroka_info[1]}, '{ship_name}', {stroka_info[3]}, {stroka_info[4]}, {stroka_info[5]}, {stroka_info[6]}, {stroka_info[7]}, {stroka_info[8]}, {stroka_info[9]}, '{country}', '{photourl}');")
    for stroka_map in sheet_for_map.itertuples():
        with connection.cursor() as cursor:
            cursor.execute(f"insert into vesselmap VALUES({stroka_map[1]}, {stroka_map[2]}, {stroka_map[3]}, timestamp '{stroka_map[4]}');")

except Exception as _ex:
    print('error:',_ex)
finally:
    if connection:
        connection.close()
        print('Connection closed')

