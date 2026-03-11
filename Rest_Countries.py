

name= userinput.strip().split()

import requests

namec= "%20".join(name)

country = requests.get(f"https://restcountries.com/v3.1/name/{namec}?fullText=true&fields=name,capital,region,subregion,population,currencies,languages,flags,timezones,latlng")

if country.status_code == 200:
        Country_data= country.json()    
        

else:
        
        print("this is not working")

"""Country Data"""

#NOTE , all data is not mandatory, I just put everything that the API and fields gave me, only the ones necessary,and if useful
#Retrieve the whole dictionary:

Country_data[0]



#Flag in png and svg

flag_png= Country_data[0]["flags"]["png"] 

flag_svg= Country_data[0]["flags"]["svg"]



#CountryName

NameCmmn= Country_data[0]["name"]["common"]

#This is for the long name

NameOff= Country_data[0]["name"]["official"]


#Name    the country (original language)

CodeNameCmmn= list(Country_data[0]["name"]["nativeName"].keys())[0]

OriginalNameCmmn= Country_data[0]["name"]["nativeName"][CodeNameCmmn]["common"]   #We know what common and official mean

OriginalNameOff=Country_data[0]["name"]["nativeName"][CodeNameCmmn]["official"]


#Currency

CurrencyCode= list(Country_data[0]["currencies"].keys())[0]

CurrencyName= Country_data[0]["currencies"][CurrencyCode]["name"]

CurrencySymbol= Country_data[0]["currencies"][CurrencyCode]["symbol"]


#Language
languagecode= list(Country_data[0]["languages"].keys())[0]

languageName= Country_data[0]["languages"][languagecode]


#More info

capital = Country_data[0]["capital"][0]

region=  Country_data[0]["region"]

subregion =  Country_data[0]["subregion"]

population=  Country_data[0]["population"]


timezones =  Country_data[0]["timezones"]

timezone =  Country_data[0]["timezones"][0]  #Some countries are very big

#Weather information


lat = Country_data[0]["latlng"][0]
lng = Country_data[0]["latlng"][1]

#Combining that data for retrieving  weather

# weather= requests.get(f"")


