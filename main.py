import folium
from folium.plugins import HeatMap
import psycopg2

host = "localhost"
port = 8000
dbname = "postgres"
user = "postgres"
password = "Son40788"

m = folium.Map(location=[34.7, -100], zoom_start=4)

ships = [folium.FeatureGroup(name=f"Корабли {hour:02d}:00", show=False).add_to(m) for hour in range(24)]
ro = [folium.FeatureGroup(name=f"Плотность {hour:02d}:00", show=False).add_to(m) for hour in range(24)]
locations = [[] for _ in range(24)]

try:
    connection = psycopg2.connect(host=host, port=port, database=dbname, user=user, password=password)
    connection.autocommit = True
    with connection.cursor() as cursor:
        for hours in range(24):
            cursor.execute(f"select * from vesselmap where extract(hour from ship_time) = {hours};")
            for ship_map in cursor.fetchall():
                cursor.execute(f"select * from vesselinfo where mmsi_pk =  {ship_map[0]};")
                ship_info=cursor.fetchone()
                folium.Marker(location=[ship_map[1], ship_map[2]], tooltip="Нажми!", popup=f'<iframe srcdoc="<img src=\'{ship_info[10]}\' width=\'300\'><li><strong>MMSI:</strong> {ship_info[0]}</li><li><strong>Позывной:</strong> {ship_info[1]}</li><li><strong>Тип корабля:</strong> {ship_info[2]}</li><li><strong>Груз:</strong> {ship_info[3]}</li><li><strong>Скорость:</strong> {ship_info[4]}</li><li><strong>Курс:</strong> {ship_info[5]}</li><li><strong>Длина:</strong> {ship_info[6]}</li><li><strong>Ширина:</strong> {ship_info[7]}</li><li><strong>Осадка:</strong> {ship_info[8]}</li><li><strong>Страна:</strong> {ship_info[9]}</li>" width="315" height="420"></iframe>', icon=folium.Icon(icon='flag'), ).add_to(ships[hours])
                locations[hours].append([ship_map[1],ship_map[2]])
except Exception as _ex:
    print('error:',_ex)
finally:
    if connection:
        connection.close()
        print('Connection closed')

for hour in range(24):
    HeatMap(locations[hour], radius=20).add_to(ro[hour])

folium.LayerControl().add_to(m)
m.save("map.html")

