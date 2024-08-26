from geopy.geocoders import Nominatim
import geopy.distance
from home.models import Distance





def get_lat_long(city):
    geolocator = Nominatim(user_agent='DistanceCalcultor')
    
    country = 'Iran'
    loc = geolocator.geocode(city+','+country)
    
    return[loc.latitude,loc.longitude]

def calculateDistance(lat1,lon1,lat2,lon2):
    coords_1 = (lat1,lon1)
    coords_2 = (lat2,lon2)
    
    return geopy.distance.geodesic(coords_1,coords_2).kilometers


def main(place1,place2):
    
    ex = Distance.objects.get(origin=place1,destination=place2)
    print('-'*90)
    print(ex)
    try:
        return ex.o_d
    except Distance.DoesNotExist: 
        position1 = get_lat_long(place1)
        position2 = get_lat_long(place2)
        
        distance = calculateDistance(position1[0],position1[1],position2[0],position2[1])
        if distance is not None:
            Distance.objects.create(origin=place1,destination=place2,o_d=distance)
        return (distance)



    # print(distance)    


