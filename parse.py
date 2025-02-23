import pandas as pd
import psycopg2
import re

pattern = r'[^\w\s]'

host = "localhost"
port = 8000
dbname = "postgres"
user = "postgres"
password = "Son40788"

sheet1 = pd.read_csv("AIStest.csv")
sheet = sheet1.fillna(0)

sheet["BaseDateTime"] = pd.to_datetime(sheet["BaseDateTime"])
sheet.info(verbose=True, show_counts=True)
#sheet.head()
sheet_sorted = sheet.sort_values(by=["BaseDateTime"])
sheet_result = sheet_sorted.groupby(["MMSI", sheet_sorted["BaseDateTime"].dt.floor("h")], as_index=False).first()
#sheet_result.info()
#sheet_result.head()

sheet_for_map = sheet_result.drop(['SOG', 'COG', 'Heading', 'VesselName', 'IMO', 'CallSign', 'VesselType', 'Status', 'Length', 'Width', 'Draft', 'Cargo', 'TransceiverClass'], axis=1)
sheet_for_map.info(verbose=True, show_counts=True)
sheet_for_map.head()

sheet_for_info = sheet_result.drop(['BaseDateTime', 'LAT', 'LON', 'Heading', 'IMO', 'CallSign', 'Status', 'TransceiverClass'], axis=1).drop_duplicates(subset=["MMSI"], keep="first")
sheet_for_info.info(verbose=True, show_counts=True)
sheet_for_info.head()

try:
    connection = psycopg2.connect(host=host, port=port, database=dbname, user=user, password=password)
    connection.autocommit = True
    for stroka_info in sheet_for_info.itertuples():
        with connection.cursor() as cursor:
            ship_name = f'{stroka_info[4]}'
            ship_name = re.sub(pattern, '',ship_name)
            cursor.execute(f"insert into vesselinfo VALUES({stroka_info[1]}, '{ship_name}', {stroka_info[5]}, {stroka_info[9]}, {stroka_info[2]}, {stroka_info[3]}, {stroka_info[6]}, {stroka_info[7]}, {stroka_info[8]});")
    for stroka_map in sheet_for_map.itertuples():
        with connection.cursor() as cursor:
            cursor.execute(f"insert into vesselmap VALUES({stroka_map[1]}, {stroka_map[3]}, {stroka_map[4]}, timestamp '{stroka_map[2]}');")

except Exception as _ex:
    print('error:',_ex)
finally:
    if connection:
        connection.close()
        print('Connection closed')

