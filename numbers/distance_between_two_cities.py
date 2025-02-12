from geopy.geocoders import Nominatim
from math import radians, cos, sin, asin, sqrt


def main():
    city_1 = input('Enter first city: ')
    city_2 = input('Enter second city: ')
    unit = input('Specify distance unit (km/m): ')
    print(f'Distance between {city_1} and {city_2} is {find_distance(city_1, city_2, unit)} in {unit}')

def find_distance(city_1, city_2, unit):
    geolocator = Nominatim(user_agent="MyApp")

    location_city_1 = geolocator.geocode(city_1)
    location_city_2 = geolocator.geocode(city_2)

    lat1 = location_city_1.latitude
    lon1 = location_city_1.longitude
    lat2 = location_city_2.latitude
    lon2 = location_city_2.longitude

    distance_in_km = round(haversine(lon1, lat1, lon2, lat2), 2)
    return distance_in_km if unit == 'km' else distance_in_km * 0.6214
    
def haversine(lon1, lat1, lon2, lat2):
    # https://stackoverflow.com/a/4913653
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r


if __name__ == "__main__":
    main()