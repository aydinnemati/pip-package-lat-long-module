import geopy
from geopy.geocoders import Nominatim
from countryinfo import CountryInfo

class GetLocation:
    def getlocation(lat, longg):
        locator = Nominatim(user_agent="myGeocoder")
        location = locator.reverse(f"{lat}, {longg}")
        # print(location.raw)
        # print(location.raw["address"]["country"])
        output = {
            "latitude": lat,
            "longitude": longg,
            "country": location.raw["address"]["country"],
            "country_code": location.raw["address"]["country_code"]
        }
        # print(output)
        return output

class Country_Info:
    def countryinfo(output):
        country_codeee = output["country_code"]
        country = CountryInfo(f"{country_codeee}").info()
        # print(country)
        output_Country_Info = {
            "country": country["name"],
            "country_code": output["country_code"],
            "latitude": output["latitude"],
            "longitude": output["longitude"],
            "languages": country["languages"],
            "population": country["population"],
            "timezones": country["timezones"]
        }
        # print(output_Country_Info)
        return output_Country_Info 
