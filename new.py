import folium

# Coordinates for the map which we want to locate
latitude = 26.7957
longitude = 82.1944

# Create a base map
my_map = folium.Map(location=[latitude, longitude], zoom_start=10)

# Coordinates for Location 1 (Ayodhya)
lat1, lon1 = 26.7953 , 82.1944
folium.Marker([lat1, lon1], popup='Shri Ram mandir').add_to(my_map)

# Coordinates for Location 2 (india)
lat2, lon2 = 20.5937 , 78.9629
folium.Marker([lat2, lon2], popup='india').add_to(my_map)

# Save the map as an HTML file
my_map.save('inactve_map.html')