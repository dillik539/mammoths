import folium
from folium import plugins
import csv
'''create map with terrain tiles style'''
mammoth_map = folium.Map(location = [40, -120], zoom_start = 3, tiles = 'Stamen Terrain')
lat_lng = [] #empty list to store latitude and longitude required for heatmap
'''read mammoth_data.csv and use the data to create markers, and add it to map'''
with open('mammoth_data.csv', 'r') as mammoth_csv:
    reader = csv.reader(mammoth_csv, quoting = csv.QUOTE_NONNUMERIC)
    '''discard the column headings'''
    firstline = reader.__next__()
    for line in reader:
        lat = line[3]
        lon = line[4]
        lat_lng.append([lat, lon]) #append a list of lat, lon
        marker_text = '%s found in %s, %s. %s' % (line[0], line[6], line[5], line[7])
        if line[1]:
            marker_text+='%s %s' % (line[1], line[2])
        marker = folium.Marker([lat, lon], popup = marker_text)
        marker.add_to(mammoth_map)
mammoth_map.save('mammoth_map.html')

'''Heatmap uses a list of [lat, lng] coordinates'''
heatmap = folium.Map(location = [40, -120], zoom_start=3)
heatmap.add_children(plugins.HeatMap(lat_lng))
heatmap.save('mammoth_heatmap.html')
