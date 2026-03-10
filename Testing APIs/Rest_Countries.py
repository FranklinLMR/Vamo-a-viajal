

name= "Dominican Republic".strip().split()

import requests

namec= "%20".join(name)

country = requests.get(f"https://restcountries.com/v3.1/name/{namec}?fullText=true&fields=name,capital,region,subregion,population,currencies,languages,flags,timezones,latlng")

if country.status_code == 200:
        Country_data= country.json()    
        

else:
        
        print("this is not working")

"""Country Data"""

#Retrieve the whole dictionary:

Country_data[0]



#Flag in png and svg

Country_data[0]["flags"]["png"]

Country_data[0]["flags"]["svg"]



#CountryName

Country_data[0]["name"]["common"]

#This is for the long name

Country_data[0]["name"]["official"]


#Name    the country (original language)

Country_data[0]["name"]["nativeName"]["spa"]["common"]   #We know what common and official mean

Country_data[0]["name"]["nativeName"]["spa"]["official"]


#Currency

CurrencyCode= list(Country_data[0]["currencies"].keys())[0]

CurrencyName= Country_data[0]["currencies"][CurrencyCode]["name"]


# weather= requests.get(f"")


