import folium
from folium.plugins import HeatMap
import psycopg2
from folium.plugins import MousePosition

host = "localhost"
port = 8000
dbname = "postgres"
user = "postgres"
password = "Son40788"

TRACKING_MODE = 'ON'
tracking_mmsi_list = [210325000,566644000,91800047,109090201,209470000,211107900,219671000,229708000,244022000,248968000]

hourlist = [1]

m = folium.Map(location=[34.7, -100], zoom_start=4)

if TRACKING_MODE == 'ON':
    tracking_ship = [folium.FeatureGroup(name=f"Отслеживаемый корабль: {tracking_mmsi}", show=False).add_to(m) for tracking_mmsi in tracking_mmsi_list]

if CLUSTER_MODE == 'ON':
    ships_group = [folium.FeatureGroup(name=f"Корабли {hour:02d}:00", show=False).add_to(m) for hour in hourlist]
    ships = [MarkerCluster(disable_clustering_at_zoom=9, spiderfy_on_max_zoom=False).add_to(ships_group[hourlist.index(hour)]) for hour in hourlist]
else:
    ships = [folium.FeatureGroup(name=f"Корабли {hour:02d}:00", show=False).add_to(m) for hour in hourlist]
ro = [folium.FeatureGroup(name=f"Плотность {hour:02d}:00", show=False).add_to(m) for hour in hourlist]
locations = [[] for hour in hourlist]

try:
    connection = psycopg2.connect(host=host, port=port, database=dbname, user=user, password=password)
    connection.autocommit = True
    with connection.cursor() as cursor:
        for hour in hourlist:
            cursor.execute(f"select * from vesselmap where extract(hour from ship_time) = {hour};")
            for ship_map in cursor.fetchall():
                cursor.execute(f"select * from vesselinfo where mmsi_pk = {ship_map[0]};")
                ship_info=cursor.fetchone()
                cursor.execute(f"select * from vesseltypeinfo where ship_type_pk = {ship_info[2]};")
                ship_type_info=cursor.fetchone()
                folium.Marker(location=[ship_map[1], ship_map[2]], tooltip="Нажми!", popup=f'<iframe srcdoc="<img src=\'{ship_info[7]}\' width=\'300\'><li><strong>MMSI:</strong> {ship_info[0]}</li><li><strong>Позывной:</strong> {ship_info[1]}</li><li><strong>Тип корабля:</strong> {ship_type_info[1]}</li><li><strong>Детали:</strong> {ship_type_info[2]}</li><li><strong>Скорость:</strong> {ship_map[4]}</li><li><strong>Курс:</strong> {ship_map[5]}</li><li><strong>Длина:</strong> {ship_info[3]}</li><li><strong>Ширина:</strong> {ship_info[4]}</li><li><strong>Осадка:</strong> {ship_info[5]}</li><li><strong>Страна:</strong> {ship_info[6]}</li>" width="315" height="420"></iframe>', icon=folium.Icon(icon='location-arrow',prefix='fa', color=f'{ship_type_info[3]}',angle=round(ship_map[5])-45)).add_to(ships[hours])
                locations[hours].append([ship_map[1],ship_map[2]])
        if TRACKING_MODE == 'ON':
            cursor.execute(f"select * from vesselmap where mmsi_fk = {tracking_mmsi};")
            for tracking_ship_map in cursor.fetchall():
                cursor.execute(f"select * from vesselinfo where mmsi_pk = {tracking_ship_map[0]};")
                tracking_ship_info=cursor.fetchone()
                cursor.execute(f"select * from vesseltypeinfo where ship_type_pk = {tracking_ship_info[2]};")
                tracking_ship_type_info = cursor.fetchone()
                folium.Marker(location=[tracking_ship_map[1], tracking_ship_map[2]], tooltip="Нажми!", popup=f'<iframe srcdoc="<img src=\'{tracking_ship_info[7]}\' width=\'300\'><li><strong>MMSI:</strong> {tracking_ship_info[0]}</li><li><strong>Время:</strong> {tracking_ship_map[3]}</li><li><strong>Позывной:</strong> {tracking_ship_info[1]}</li><li><strong>Тип корабля:</strong> {tracking_ship_type_info[1]}</li><li><strong>Детали:</strong> {tracking_ship_type_info[2]}</li><li><strong>Скорость:</strong> {tracking_ship_map[4]}</li><li><strong>Курс:</strong> {tracking_ship_map[5]}</li><li><strong>Длина:</strong> {tracking_ship_info[3]}</li><li><strong>Ширина:</strong> {tracking_ship_info[4]}</li><li><strong>Осадка:</strong> {tracking_ship_info[5]}</li><li><strong>Страна:</strong> {tracking_ship_info[6]}</li>" width="315" height="420"></iframe>',icon=folium.Icon(icon='location-arrow', prefix='fa', color=f'{tracking_ship_type_info[3]}',angle=round(tracking_ship_map[5]) - 45)).add_to(tracking_ship)
except Exception as _ex:
    print('error:',_ex)
finally:
    if connection:
        connection.close()
        print('Connection closed')

for hour in range(24):
    HeatMap(locations[hour], radius=20).add_to(ro[hour])

folium.LayerControl().add_to(m)

MousePosition(position="bottomleft",separator=" | ",lng_first=True, num_digits=5,prefix="Текущие координаты:",empty_string="NaN").add_to(m)

m.save("map.html")

