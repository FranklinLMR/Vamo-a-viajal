import flet as ft
import requests
 


userinput= "Dominican Republic"
#
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










 
def main(page: ft.Page):
    
    
    #fonts
    page.fonts = {
        "Main": "fredoka-latin-700-normal.ttf"
    }
 
    page.theme = ft.Theme(font_family="Main")
    page.title= "Via Py"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#f3f7ff"
    page.update()
 
#Title
    title = ft.Text("Country Search", size=80, color="#12366b", align=ft.Alignment.CENTER, )
 
#search bar
 
    search = ft.SearchBar(bar_hint_text="Search a Country...", align=ft.Alignment.CENTER, bar_bgcolor="#FFFFFF")
 
#White container
    #collumn1
    Flag = ft.Container(ft.Image(src="FlagDR.png"), width=200)
    
    CName = ft.Text(value="Country Name", size = 20, color="#12366b")
    NameAPI = ft.Text(value=f"{NameCmmn}", size = 15, color= "#000000")
 
    CapName = ft.Text(value="Capital City", size = 20, color="#12366b")
    CapAPI = ft.Text(value=f"{capital}", size = 15, color= "#000000")
 
    Region = ft.Text(value="Region", size = 20, color="#12366b")
    RegAPI = ft.Text(value=f"{region}", size = 15, color= "#000000")
 
    SubRegion = ft.Text(value="Sub Region", size = 20, color="#12366b")
    SRegAPI = ft.Text(value=f"{subregion}", size = 15, color= "#000000")
 
#divider made by a container (im so smart i know) (Or maybe im just to lazy to investigate if there a vertical divider)
    divide = ft.Container(bgcolor="#000000", height=500, width=2)
 
    column1 = ft.Column(controls=[ Flag,
        ft.Container(height=10),
        CName, NameAPI,
        ft.Container(height=10),
        CapName, CapAPI,
        ft.Container(height=10),
        Region, RegAPI,
        ft.Container(height=10),
        SubRegion, SRegAPI], spacing=1, alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    
#I know I can do it another way but like this is easier for me to then change the value of the lorem ipsum part ;)
 
    #column2
    Popu = ft.Text(value="Population", size = 30, color="#12366b")
    PopuAPI = ft.Text(value=f"{population}", size = 20, color= "#000000")
 
    Curre = ft.Text(value="Currency", size = 30, color="#12366b")
    CurreAPI = ft.Text(value=f"{CurrencyName} ({CurrencyCode})", size = 20, color= "#000000")
 
    Lan = ft.Text(value="Language", size = 30, color="#12366b")
    LanAPI = ft.Text(value=f"{languageName}", size = 20, color= "#000000")
 
    column2 = ft.Column(
    controls=[
        Popu,PopuAPI,
        ft.Container(height=50),
        Curre, CurreAPI,
        ft.Container(height=50),
        Lan, LanAPI
    ]
)
 
    #column3
    Visa = ft.Text(value="Basic Visa", size = 30, color="#12366b")
    VisaAPI = ft.Text(value="Lorem Ipsum", size = 20, color= "#000000")
 
    cCode = ft.Text(value="Country Code", size = 30, color="#12366b")
    CCodeAPI = ft.Text(value="Lorem Ipsum", size = 20, color= "#000000")
 
    column3 = ft.Column(
    controls=[
        Visa,VisaAPI,
        ft.Container(height=50),
        cCode,
        CCodeAPI
    ]
)
 
    #column4 I forgot to add it. (Im so done teacher)
    Tzone = ft.Text(value="Time Zone", size = 30, color="#12366b")
    TZoneAPI = ft.Text(value=f"{timezones[0]}", size = 20, color= "#000000")
 
    Weather = ft.Text(value="Weather", size = 30, color="#12366b")
    WeatherAPI = ft.Text(value="Lorem Ipsum", size = 20, color= "#000000")
 
    LocTime = ft.Text(value="Local Time", size = 30, color="#12366b")
    LocTimeAPI = ft.Text(value="Lorem Ipsum", size = 20, color= "#000000")
 
    column4 = ft.Column(
        controls=[
            Tzone, TZoneAPI,
            ft.Container(height=50),
            Weather, WeatherAPI,
            ft.Container(height=50),
            LocTime, LocTimeAPI
        ],
        alignment=ft.MainAxisAlignment.START
    )    
    #White container
    wContainer = ft.Container(content=ft.Row(
            controls=[column1, divide, column4, column2, column3], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
            height=525,
            width = 1250,
            bgcolor="#FFFFFF",
            border_radius=10,
            padding=50,align=ft.Alignment.BOTTOM_CENTER)
    
    #found documentation for the space_evenly im so lost with this new version
    
    #space container (pls dont question me)
    space5 = ft.Container(height=5)
    space10 = ft.Container(height=10)
 
    #Main container
    blueCont = ft.Container(content=ft.Column(
        controls=[space10, search, space5, wContainer],
        spacing=20),
            height=700,
            width = 1350,
            bgcolor="#12366b",
            border_radius=10, align=ft.Alignment.BOTTOM_CENTER)
    
    Whole_page= ft.Column(controls=[title, blueCont])
    page.add(Whole_page)
 
 
ft.run(main, assets_dir="assets")    
 