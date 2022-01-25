from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="url_for_map")

for each in myList:
    location = geolocator.geocode(each)
    if location != None:
        print(each+"_",(location.latitude, location.longitude))
