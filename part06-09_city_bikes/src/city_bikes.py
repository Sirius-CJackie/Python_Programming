# tee ratkaisu tänne
# Write your solution here
import math

def get_station_data(filename):
    stations = {}
    with open(filename) as file:  
        for line in file:
            parts = line.strip().split(';')
            if parts[0] == 'Longitude':
                continue
            name = parts[3]
            longitude = float(parts[0])
            latitude = float(parts[1])
            stations[name] = (longitude, latitude)

    return stations

def distance(stations, station1, station2):
    lon1, lat1 = stations[station1]
    lon2, lat2 = stations[station2]
    x = (lon1 - lon2) * 55.26
    y = (lat1 - lat2) * 111.2
    distance = math.sqrt(x**2 + y**2)
    return distance

def greatest_distance(stations):
    max_distance = 0
    max_station1 = None
    max_station2 = None
    station_names = list(stations.keys())
    for i in range(len(station_names)):
        for j in range(i + 1, len(station_names)):
            d = distance(stations, station_names[i], station_names[j])
            if d > max_distance:
                max_distance = d
                max_station1 = station_names[i]
                max_station2 = station_names[j]

    return max_station1, max_station2, max_distance

