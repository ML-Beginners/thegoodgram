#Import Library
import folium
import pandas as pd

# Dataset
states = pd.read_csv('states.csv')

#Create base map
map = folium.Map(location=[28.7041,77.1025], zoom_start = 6, tiles= “CartoDB dark_matter”)

for loc in zip(states['Latitude'], states['Longitude']):
    folium.Marker(location=loc, icon=folium.Icon(color = 'green')).add_to(map)

#Save the map
map.save("map.html")
