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
        folium.Marker(location=[lat, lon], tooltip="Нажми!", popup=popup, icon=folium.Icon(icon='flag')).add_to(ship)
for mll in l1stmll:
    print(mll)

HeatMap(locations, radius=20).add_to(ro)
folium.LayerControl().add_to(m)
m.save("picture.html")
