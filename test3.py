import folium

map = folium.Map(location=[55.751244, 37.618423], zoom_start=9)

folium.Marker([55.751244, 37.618423], popup='Moscov').add_to(map)

map.save("moscow.html")