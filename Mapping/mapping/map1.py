import folium

map = folium.Map(location = [51.525, -9.583], zoom_start = 6, tiles = "Mapbox Bright")

fg = folium.FeatureGroup( name = "My Map")
fg.add_child(folium.Marker(location = [51.525, -9.583], popup = "Marker", icon = folium.Icon(color = 'green')))
map.add_child(fg)

map.save("Map1.html")
