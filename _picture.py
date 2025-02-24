from pyais.stream import FileReaderStream
import re
import folium
from folium.plugins import HeatMap
import branca
from folium import IFrame
m = folium.Map(location=[0, 0], zoom_start=3)
l1st = []
ship = folium.FeatureGroup(name="Корабли", show=False).add_to(m)
ro = folium.FeatureGroup(name="Плотность", show=False).add_to(m)
mmsi = 205755000
ship_name = 'ORION'
ship_type = 90
ship_cargo = 90
ship_sog = 0
ship_cog = 171.5
ship_length = 215
ship_width = 50
ship_draft = 10.8
ship_country = 'Belgium'
ship_imageurl = 'https://static.vesselfinder.net/ship-photo/9825453-371197000-92a2078295df48dd3cc6b62b4ab8aa99/1?v1'
with FileReaderStream("./20241009_AIS.txt") as stream:
    for msg in stream:
        decoded = msg.decode()
        l1st.append(decoded)
pattern = re.compile(r"mmsi=(\d+).*?lon=([\d.-]+).*?lat=([\d.-]+)")
l1stmll = []
locations=[]
for message in l1st:
    match = pattern.search(str(message))
    if match:
        mmsi = match.group(1)
        lon = match.group(2)
        lat = match.group(3)
        locations.append([lat,lon])
        try:
            with open(f'{mmsi}.html', 'r', encoding='utf-8') as file:
                html = file.read()
        except FileNotFoundError:
            with open('error.html', 'r', encoding='utf-8') as file:
                html = file.read()
        popup = folium.Popup(html, max_width=1000)
        folium.Marker(location=[lat, lon], tooltip="Нажми!", popup=f'<iframe srcdoc="<img src=\'{ship_imageurl}\' width=\'300\'><li><strong>MMSI:</strong> {mmsi}</li><li><strong>Позывной:</strong> {ship_name}</li><li><strong>Тип корабля:</strong> {ship_type}</li><li><strong>Груз:</strong> {ship_cargo}</li><li><strong>Скорость:</strong> {ship_sog}</li><li><strong>Курс:</strong> {ship_cog}</li><li><strong>Длина:</strong> {ship_length}</li><li><strong>Ширина:</strong> {ship_width}</li><li><strong>Осадка:</strong> {ship_draft}</li><li><strong>Страна:</strong> {ship_country}</li>" width="315" height="420"></iframe>', icon=folium.Icon(icon='flag')).add_to(ship)
for mll in l1stmll:
    print(mll)

HeatMap(locations, radius=20).add_to(ro)
folium.LayerControl().add_to(m)
m.save("picture.html")
