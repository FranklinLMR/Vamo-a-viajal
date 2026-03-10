import requests

country = requests.get("https://restcountries.com/v3.1/all?fields=name,flags")

if country.status_code == 200:
        Country_data= country.json()
        

else:
        
        print("this is not working")



print(Country_data[0])