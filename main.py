import folium
from folium.plugins import HeatMap
import parse

m = folium.Map(location=[34.7, -100], zoom_start=4)
ship00 = folium.FeatureGroup(name="Корабли 00:00", show=False).add_to(m)
ship01 = folium.FeatureGroup(name="Корабли 01:00", show=False).add_to(m)
ship02 = folium.FeatureGroup(name="Корабли 02:00", show=False).add_to(m)
ship03 = folium.FeatureGroup(name="Корабли 03:00", show=False).add_to(m)
ship04 = folium.FeatureGroup(name="Корабли 04:00", show=False).add_to(m)
ship05 = folium.FeatureGroup(name="Корабли 05:00", show=False).add_to(m)
ship06 = folium.FeatureGroup(name="Корабли 06:00", show=False).add_to(m)
ship07 = folium.FeatureGroup(name="Корабли 07:00", show=False).add_to(m)
ship08 = folium.FeatureGroup(name="Корабли 08:00", show=False).add_to(m)
ship09 = folium.FeatureGroup(name="Корабли 09:00", show=False).add_to(m)
ship10 = folium.FeatureGroup(name="Корабли 10:00", show=False).add_to(m)
ship11 = folium.FeatureGroup(name="Корабли 11:00", show=False).add_to(m)
ship12 = folium.FeatureGroup(name="Корабли 12:00", show=False).add_to(m)
ship13 = folium.FeatureGroup(name="Корабли 13:00", show=False).add_to(m)
ship14 = folium.FeatureGroup(name="Корабли 14:00", show=False).add_to(m)
ship15 = folium.FeatureGroup(name="Корабли 15:00", show=False).add_to(m)
ship16 = folium.FeatureGroup(name="Корабли 16:00", show=False).add_to(m)
ship17 = folium.FeatureGroup(name="Корабли 17:00", show=False).add_to(m)
ship18 = folium.FeatureGroup(name="Корабли 18:00", show=False).add_to(m)
ship19 = folium.FeatureGroup(name="Корабли 19:00", show=False).add_to(m)
ship20 = folium.FeatureGroup(name="Корабли 20:00", show=False).add_to(m)
ship21 = folium.FeatureGroup(name="Корабли 21:00", show=False).add_to(m)
ship22 = folium.FeatureGroup(name="Корабли 22:00", show=False).add_to(m)
ship23 = folium.FeatureGroup(name="Корабли 23:00", show=False).add_to(m)
ro00 = folium.FeatureGroup(name="Плотность 00:00", show=False).add_to(m)
ro01 = folium.FeatureGroup(name="Плотность 01:00", show=False).add_to(m)
ro02 = folium.FeatureGroup(name="Плотность 02:00", show=False).add_to(m)
ro03 = folium.FeatureGroup(name="Плотность 03:00", show=False).add_to(m)
ro04 = folium.FeatureGroup(name="Плотность 04:00", show=False).add_to(m)
ro05 = folium.FeatureGroup(name="Плотность 05:00", show=False).add_to(m)
ro06 = folium.FeatureGroup(name="Плотность 06:00", show=False).add_to(m)
ro07 = folium.FeatureGroup(name="Плотность 07:00", show=False).add_to(m)
ro08 = folium.FeatureGroup(name="Плотность 08:00", show=False).add_to(m)
ro09 = folium.FeatureGroup(name="Плотность 09:00", show=False).add_to(m)
ro10 = folium.FeatureGroup(name="Плотность 10:00", show=False).add_to(m)
ro11 = folium.FeatureGroup(name="Плотность 11:00", show=False).add_to(m)
ro12 = folium.FeatureGroup(name="Плотность 12:00", show=False).add_to(m)
ro13 = folium.FeatureGroup(name="Плотность 13:00", show=False).add_to(m)
ro14 = folium.FeatureGroup(name="Плотность 14:00", show=False).add_to(m)
ro15 = folium.FeatureGroup(name="Плотность 15:00", show=False).add_to(m)
ro16 = folium.FeatureGroup(name="Плотность 16:00", show=False).add_to(m)
ro17 = folium.FeatureGroup(name="Плотность 17:00", show=False).add_to(m)
ro18 = folium.FeatureGroup(name="Плотность 18:00", show=False).add_to(m)
ro19 = folium.FeatureGroup(name="Плотность 19:00", show=False).add_to(m)
ro20 = folium.FeatureGroup(name="Плотность 20:00", show=False).add_to(m)
ro21 = folium.FeatureGroup(name="Плотность 21:00", show=False).add_to(m)
ro22 = folium.FeatureGroup(name="Плотность 22:00", show=False).add_to(m)
ro23 = folium.FeatureGroup(name="Плотность 23:00", show=False).add_to(m)

locations00 = []
locations01 = []
locations02 = []
locations03 = []
locations04 = []
locations05 = []
locations06 = []
locations07 = []
locations08 = []
locations09 = []
locations10 = []
locations11 = []
locations12 = []
locations13 = []
locations14 = []
locations15 = []
locations16 = []
locations17 = []
locations18 = []
locations19 = []
locations20 = []
locations21 = []
locations22 = []
locations23 = []

for stroka in parse.sheet_for_map.itertuples():
    mmsi = stroka[1]
    hours = stroka[2].hour
    lat, lon = stroka[3], stroka[4]
    if hours == 0:
            folium.Marker(location=[lat, lon], tooltip="Нажми!", popup=mmsi, icon=folium.Icon(icon='flag'), ).add_to(ship00)
            locations00.append([lat,lon])
    if hours == 1:
            folium.Marker(location=[lat, lon], tooltip="Нажми!", popup=mmsi, icon=folium.Icon(icon='flag'), ).add_to(ship01)
            locations01.append([lat,lon])
    if hours == 2:
            folium.Marker(location=[lat, lon], tooltip="Нажми!", popup=mmsi, icon=folium.Icon(icon='flag'), ).add_to(ship02)
            locations02.append([lat,lon])
    if hours == 3:
            folium.Marker(location=[lat, lon], tooltip="Нажми!", popup=mmsi, icon=folium.Icon(icon='flag'), ).add_to(ship03)
            locations03.append([lat,lon])
    if hours == 4:
            folium.Marker(location=[lat, lon], tooltip="Нажми!", popup=mmsi, icon=folium.Icon(icon='flag'), ).add_to(ship04)
            locations04.append([lat,lon])
    if hours == 5:
            folium.Marker(location=[lat, lon], tooltip="Нажми!", popup=mmsi, icon=folium.Icon(icon='flag'), ).add_to(ship05)
            locations05.append([lat,lon])
    if hours == 6:
            folium.Marker(location=[lat, lon], tooltip="Нажми!", popup=mmsi, icon=folium.Icon(icon='flag'), ).add_to(ship06)
            locations06.append([lat,lon])
    if hours == 7:
            folium.Marker(location=[lat, lon], tooltip="Нажми!", popup=mmsi, icon=folium.Icon(icon='flag'), ).add_to(ship07)
            locations07.append([lat,lon])
    if hours == 8:
            folium.Marker(location=[lat, lon], tooltip="Нажми!", popup=mmsi, icon=folium.Icon(icon='flag'), ).add_to(ship08)
            locations08.append([lat,lon])
    if hours == 9:
            folium.Marker(location=[lat, lon], tooltip="Нажми!", popup=mmsi, icon=folium.Icon(icon='flag'), ).add_to(ship09)
            locations09.append([lat,lon])
    if hours == 10:
            folium.Marker(location=[lat, lon], tooltip="Нажми!", popup=mmsi, icon=folium.Icon(icon='flag'), ).add_to(ship10)
            locations10.append([lat,lon])
    if hours == 11:
            folium.Marker(location=[lat, lon], tooltip="Нажми!", popup=mmsi, icon=folium.Icon(icon='flag'), ).add_to(ship11)
            locations11.append([lat,lon])
    if hours == 12:
            folium.Marker(location=[lat, lon], tooltip="Нажми!", popup=mmsi, icon=folium.Icon(icon='flag'), ).add_to(ship12)
            locations12.append([lat,lon])
    if hours == 13:
            folium.Marker(location=[lat, lon], tooltip="Нажми!", popup=mmsi, icon=folium.Icon(icon='flag'), ).add_to(ship13)
            locations13.append([lat,lon])
    if hours == 14:
            folium.Marker(location=[lat, lon], tooltip="Нажми!", popup=mmsi, icon=folium.Icon(icon='flag'), ).add_to(ship14)
            locations14.append([lat,lon])
    if hours == 15:
            folium.Marker(location=[lat, lon], tooltip="Нажми!", popup=mmsi, icon=folium.Icon(icon='flag'), ).add_to(ship15)
            locations15.append([lat,lon])
    if hours == 16:
            folium.Marker(location=[lat, lon], tooltip="Нажми!", popup=mmsi, icon=folium.Icon(icon='flag'), ).add_to(ship16)
            locations16.append([lat,lon])
    if hours == 17:
            folium.Marker(location=[lat, lon], tooltip="Нажми!", popup=mmsi, icon=folium.Icon(icon='flag'), ).add_to(ship17)
            locations17.append([lat,lon])
    if hours == 18:
            folium.Marker(location=[lat, lon], tooltip="Нажми!", popup=mmsi, icon=folium.Icon(icon='flag'), ).add_to(ship18)
            locations18.append([lat,lon])
    if hours == 19:
            folium.Marker(location=[lat, lon], tooltip="Нажми!", popup=mmsi, icon=folium.Icon(icon='flag'), ).add_to(ship19)
            locations19.append([lat,lon])
    if hours == 20:
            folium.Marker(location=[lat, lon], tooltip="Нажми!", popup=mmsi, icon=folium.Icon(icon='flag'), ).add_to(ship20)
            locations20.append([lat,lon])
    if hours == 21:
            folium.Marker(location=[lat, lon], tooltip="Нажми!", popup=mmsi, icon=folium.Icon(icon='flag'), ).add_to(ship21)
            locations21.append([lat,lon])
    if hours == 22:
            folium.Marker(location=[lat, lon], tooltip="Нажми!", popup=mmsi, icon=folium.Icon(icon='flag'), ).add_to(ship22)
            locations22.append([lat,lon])
    if hours == 23:
            folium.Marker(location=[lat, lon], tooltip="Нажми!", popup=mmsi, icon=folium.Icon(icon='flag'), ).add_to(ship23)
            locations23.append([lat,lon])

HeatMap(locations00, radius=20).add_to(ro00)
HeatMap(locations01, radius=20).add_to(ro01)
HeatMap(locations02, radius=20).add_to(ro02)
HeatMap(locations03, radius=20).add_to(ro03)
HeatMap(locations04, radius=20).add_to(ro04)
HeatMap(locations05, radius=20).add_to(ro05)
HeatMap(locations06, radius=20).add_to(ro06)
HeatMap(locations07, radius=20).add_to(ro07)
HeatMap(locations08, radius=20).add_to(ro08)
HeatMap(locations09, radius=20).add_to(ro09)
HeatMap(locations10, radius=20).add_to(ro10)
HeatMap(locations11, radius=20).add_to(ro11)
HeatMap(locations12, radius=20).add_to(ro12)
HeatMap(locations13, radius=20).add_to(ro13)
HeatMap(locations14, radius=20).add_to(ro14)
HeatMap(locations15, radius=20).add_to(ro15)
HeatMap(locations16, radius=20).add_to(ro16)
HeatMap(locations17, radius=20).add_to(ro17)
HeatMap(locations18, radius=20).add_to(ro18)
HeatMap(locations19, radius=20).add_to(ro19)
HeatMap(locations20, radius=20).add_to(ro20)
HeatMap(locations21, radius=20).add_to(ro21)
HeatMap(locations22, radius=20).add_to(ro22)
HeatMap(locations23, radius=20).add_to(ro23)

folium.LayerControl().add_to(m)
m.save("map.html")
