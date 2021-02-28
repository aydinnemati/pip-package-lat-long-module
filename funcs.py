from classes import GetLocation, Country_Info

def LatLong(lat: float, longg: float):

    address = GetLocation.getlocation(lat, longg)
    address_info = Country_Info.countryinfo(address)
    return address_info

