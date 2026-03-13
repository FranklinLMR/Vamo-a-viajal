import flet as ft
import requests
import os
import subprocess
import flet as ft
import asyncio
import datetime
 
 
def main(page: ft.Page):
 
    def show_mainpage(e):
        page.controls.clear()
        page.add(Second_Page)
        page.update()
 
    def show_secondpage(e):
        page.controls.clear()
        page.add(Second_Page)
        page.update()
    
    def Show_thirdpage(e):
        page.controls.clear()
        page.add(Third_Page)
        page.update()
 
    #def countrysearch(e):
        #secondpath= os.path.join(os.path.dirname(__file__), "secondpage.py")
        #subprocess.Popen(["python3", secondpath])
        #page.window.close()
    
    #def bookatrip(e):
        #thirdpath= os.path.join(os.path.dirname(__file__), "thirdpage.py")
        #subprocess.Popen(["python3", thirdpath])
        #page.window.close()
        
    #fonts
    page.fonts = {
        "Main": "fredoka-latin-700-normal.ttf"
    }
    page.window.full_screen = True
    page.theme = ft.Theme(font_family="Main")
    page.title= "Via Py"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
 
    page.bgcolor = "#f3f7ff"
    page.expand=True
    page.padding= -29
    page.update()
 
#main page image
    plane_image= ft.Image(
        src="Plane2.jpg",
        visible=True,
        width=635,
        height=544.5,
        scale= 1.55 ,
        expand=True,
        
        
        )
 
#logo image
    logo_image = ft.Image(
        src="Logo.png",
        visible= True,
        # top = 35,
        # right = 700,
        width= 700,
        height=400,
        scale=0.85,
        
    )
    
 
#buttons in main page
 
    #blueContainerfor real
    ButtonA= ft.Container(on_click= show_secondpage, content=ft.Image(src="Tripbutton.png"),scale=2, ink= True, width=300, height=60, margin=40, border_radius=100)
    ButtonB= ft.Container(on_click= Show_thirdpage, content=ft.Image(src="Countrybutton.png"),scale=2
                        , ink=True, width=300, height=60, margin=40, border_radius=100)
 
    # Button1 = ft.Button(content=ft.Text(value="Book a Flight!"), icon=ft.Icons.AIRPLANEMODE_ON, width=600, height=50)
    # Button2 = ft.Button(content=ft.Text(value="Country Search"), icon=ft.Icons.MY_LOCATION,width=400, height=50)
    ColumnLeft1 = ft.Column(controls=[ButtonA, ButtonB], horizontal_alignment=ft.CrossAxisAlignment.CENTER,  spacing=20, margin=40)
    ColumnLeft = ft.Column(controls=[logo_image, ColumnLeft1], horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    ColumnRight = ft.Column(controls=[plane_image],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER)
 
    Whole_page= ft.Row(controls=[ColumnLeft, ColumnRight],spacing=220, expand= True)
    page.add(Whole_page)
 
#-----------------SECOND PAGE-------------------#
 
    RegionalVisaInfo= {"Americas": "From Canada to South America, entry rules vary a lot; \nmany Latin American countries are relatively flexible for regional visitors, \nwhile the U.S. and Canada usually require advance visas or electronic authorizations.",
    "Europe": "Most European destinations are part of the Schengen Area; \nmany travelers need a Schengen visa obtained before arrival,\n though some nationalities get short-stay visa-free access.",
    "Asia": "Asia mixes very easy and very strict countries;\n some offer visa-free or visa on arrival,\n others require detailed advance visa applications.",
    "Africa": "Many African countries require a visa or eVisa before departure,\n and may ask for vaccinations,\n return tickets, and proof of accommodation.",
    "Oceania": "Australia and New Zealand rely on electronic visas or travel authorizations,\n while many Pacific islands have more relaxed but still limited-stay entry rules.",
    }
    async def SubmittedText(e):
 
            userinput=(e.control.value).lower()
            name= userinput.strip().split()
 
            namec= "%20".join(name)
 
            country = requests.get(f"https://restcountries.com/v3.1/name/{namec}?fullText=true&fields=name,capital,region,subregion,population,currencies,languages,flags,timezones,latlng,cca2,cca3,idd")
 
            if country.status_code == 200:
                Country_data= country.json()    
                    
                #Flag in png and svg
                flag_png= Country_data[0]["flags"]["png"]
 
                #CountryName
                NameCmmn= Country_data[0]["name"]["common"]
 
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
 
 
 
                #Country Code
                Ccode = Country_data[0]["cca3"]
                C2code = Country_data[0]["cca2"]
 
                #Number code
                Noocode= Country_data[0]["idd"]["root"]
 
                #Weather information
                lat = Country_data[0]["latlng"][0]
                lng = Country_data[0]["latlng"][1]
 
                #Combining that data for retrieving  weather
                url = f"https://api.open-meteo.com/v1/forecast?latitude={Country_data[0]['latlng'][0]}&longitude={Country_data[0]['latlng'][1]}&daily=temperature_2m_min,temperature_2m_max,apparent_temperature_max,apparent_temperature_min,precipitation_sum,precipitation_probability_max,weather_code,sunrise,sunset&timezone=auto"
                weather = requests.get(url)
                Wdata = weather.json()
                daily= Wdata["daily"]
                lines=[]
 
                for i in range(3):
                    date= daily["time"][i]
                    t_min= daily["temperature_2m_min"][i]
                    t_max= daily["temperature_2m_max"][i]
                    rainprec= daily["precipitation_sum"][i]
                    rainprob= daily["precipitation_probability_max"][i]
                    sunrise= daily["sunrise"][i][-5:]
                    sunset=daily["sunset"][i][-5:]
                    
                    line= (
                        f"{date}: {t_min}-{t_max}°C, "
                        f"rain {rainprec} mm ({rainprob}%), "
                        f"sun {sunrise}-{sunset}"
                    )
                    lines.append(line)
 
                #Local Time
                LocaltimeAPI= requests.get(f"https://timeapi.io/api/v1/time/current/coordinate?latitude={Country_data[0]['latlng'][0]}&longitude={Country_data[0]['latlng'][1]}")
                TimeData=LocaltimeAPI.json()
 
                #Changing content
                Flag.content.src= flag_png
 
                NameAPI.value = NameCmmn
                CapAPI.value = capital
                RegAPI.value = region
                SRegAPI.value= subregion
                PopuAPI.value =f"{population:,}"
                CurreAPI.value= f"{CurrencyName} ({CurrencyCode})"
                LanAPI.value= languageName
                CCodeAPI.value= f"{Ccode}; No. Code: {Noocode}"
                TZoneAPI.value= timezone
                VisaAPI.value= f"Passport: {C2code}\nRegional info: {RegionalVisaInfo[region]}"
                
                LocTimeAPI.value= f"{TimeData["time"][:-10]}"
 
 
                #Weather Change
 
                WeatherAPI.value= "\n".join(lines)
 
            elif e.control.value == "return":
                search.bar_hint_text= "Returning to main menu..."
                e.control.value= ""
                page.update()
                await asyncio.sleep(2)
                show_mainpage()
                page.window.close()
 
            else:
                    
                    print("this is not working")
 
            """Country Data"""
            page.update()
    #Title
    title = ft.Text("Country Search", size=80, color="#12366b", align=ft.Alignment.CENTER, )
 
    #search bar
 
    search = ft.SearchBar(bar_hint_text="Search a Country...                                                                                                       (Type 'menu' to return)",
                            align=ft.Alignment.CENTER,
                            bar_bgcolor="#FFFFFF",
                            bar_text_style=ft.TextStyle(color= "#516a8f"),
                            on_submit=SubmittedText
                            )
 
    #White container
        #collumn1
    Flag = ft.Container(ft.Image(src="FlagDR.png"), width=200)
        
    CName = ft.Text(value="Country Name", size = 20, color="#12366b")
    NameAPI = ft.Text(value=f"Search a country", size = 15, color= "#000000")
 
    CapName = ft.Text(value="Capital City", size = 20, color="#12366b")
    CapAPI = ft.Text(value=f"Search a country", size = 15, color= "#000000")
 
    Region = ft.Text(value="Region", size = 20, color="#12366b")
    RegAPI = ft.Text(value=f"Search a country", size = 15, color= "#000000")
 
    SubRegion = ft.Text(value="Sub Region", size = 20, color="#12366b")
    SRegAPI = ft.Text(value=f"Search a country", size = 15, color= "#000000")
 
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
    PopuAPI = ft.Text(value=f"Search a country", size = 20, color= "#000000")
 
    Curre = ft.Text(value="Currency", size = 30, color="#12366b")
    CurreAPI = ft.Text(value=f"Search a country ()", size = 20, color= "#000000")
 
    Lan = ft.Text(value="Language", size = 30, color="#12366b")
    LanAPI = ft.Text(value=f"Search a country", size = 20, color= "#000000")
 
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
    VisaAPI = ft.Text(value="Seach a country", size = 12    , color= "#000000")
 
    cCode = ft.Text(value="Country Code", size = 30, color="#12366b")
    CCodeAPI = ft.Text(value="Search a country", size = 20, color= "#000000")
 
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
    TZoneAPI = ft.Text(value=f"Search a country", size = 20, color= "#000000")
 
    Weather = ft.Text(value="Weather", size = 30, color="#12366b")
    WeatherAPI = ft.Text(value="Search a country", size = 12, color= "#000000")
 
    LocTime = ft.Text(value="Local Time", size = 30, color="#12366b")
    LocTimeAPI = ft.Text(value="Search a country    ", size = 20, color= "#000000")
 
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
        
    Second_Page= ft.Column(controls=[title, blueCont])
 
 
#---------------- third page -----------------------------#
 
    DataUser=["","","",""]
    def mainmenu(e):
            secondpath= os.path.join(os.path.dirname(__file__), "main.py")
            subprocess.Popen(["python3", secondpath])
            page.window.close()
 
    def SaveName(e):
            
            DataUser[0]=e.control.value
 
    def SaveNotes(e):
            DataUser[2]=e.control.value
        
    def SaveID(e):
            DataUser[1]=e.control.value
 
        
    def submit(e):
            if DepartAPI.value and ArriveAPI.value != "":
                try:
                    with open(f"DataSubmitted1.txt", "w") as file:   #This is completely bad because it is better for sql
                        file.write(f"---User-Plan---\nName: {DataUser[0]}\nID or passport: {DataUser[1]}\nCountry Code: {DataUser[3]}\nDeparture Date: {DepartAPI.value}\nReturn Date: {ArriveAPI.value}")
                except:
                    for f in range(10):
                        print("Error, Missing data")
            else:
                for f in range(10):
                        print("Error, Missing data")
 
    def handle_change(e: ft.Event[ft.DatePicker]):
            l= int(e.control.value.strftime("%d"))
            m= int(e.control.value.strftime("%m"))
            print(m)
            de.first_date = datetime.datetime(year=today.year, month=m, day=l+1)
            DepartAPI.value=f"{e.control.value.strftime('%m/%d/%Y')}"
            Duration2.visible=True
            DurrationAPI.visible=False
            page.update()
 
    def handle_change2(e: ft.Event[ft.DatePicker]):
            ArriveAPI.value=f"{e.control.value.strftime('%m/%d/%Y')}"
 
            Reset2.visible = True
            page.update()
        
    def resett(e):
            d.first_date=datetime.datetime(year=today.year, month=today.month, day=today.day+1)
            de. first_date=datetime.datetime(year=today.year, month=today.month, day=today.day+1)
            Duration2.visible=False
            Durration.visible=True
            ArriveAPI.value=""
            DepartAPI.value=""
            page.update()
 
    def Drop(e):
            e.control.value
            DataUser[3]=e.control.value
 
    today = datetime.datetime.now()
 
    d = ft.DatePicker(
            first_date=datetime.datetime(year=today.year, month=today.month, day=today.day+1),
            last_date=datetime.datetime(year=today.year, month=today.month+2    , day=20),
            on_change=handle_change
        )
    de = ft.DatePicker(
            first_date=datetime.datetime(year=today.year, month=today.month, day=today.day+1),
            last_date=datetime.datetime(year=today.year, month=today.month+2, day=20),
            on_change=handle_change2
 
        )
    Title = ft.Text("Book a flight! ", size=80, color="#12366b", align=ft.Alignment.CENTER, )
 
    Profile = ft.Container(ft.Image(src="profile.JPG"), width=200)
    Back= ft.Button(content="Main Menu", on_click= mainmenu)
    Submit= ft.Button(content="Submit", on_click=submit)
 
    Options2= ft.Row(controls=[Back, Profile, Submit], alignment= ft.MainAxisAlignment.CENTER)
 
 
    PName = ft.Text(value="Full Name", size = 20, color="#12366b")
    NameAPI = ft.TextField(label="Insert your name", color= "#000000", max_length= 50, on_submit= SaveName)
 
    IDNumber = ft.Text(value="ID Number", size = 20, color="#12366b")
    IDAPI = ft.TextField(label="Insert your Passport or ID number",  color= "#000000", max_length=30, on_submit= SaveID)   
 
    divide = ft.Container(bgcolor="#000000", height=500, width=2)
 
    column1 = ft.Column(controls=[ Title,
            ft.Container(height=10),
            PName, NameAPI,
            ft.Container(height=10),
            IDNumber, IDAPI,
            ft.Container(height=10),
            ], spacing=1, alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        
        #2
 
        
    count= requests.get("https://restcountries.com/v3.1/all?fields=name,cca2")
    cdata =count.json()
 
    Plan = ft.Text(value="Plan your trip", size = 30, color="#12366b")
    PlanAPI = ft.Dropdown(
            label="Select a country", editable= True,   
            width=200,
            options = [ft.dropdown.Option(key=c["cca2"], text=c["name"]["common"]) for c in cdata],
            on_select= Drop, text_style= ft.TextStyle( color="#516a8f" )
        )
 
    Durration = ft.Text(value="Set Duration", size = 20, color="#12366b")
    DurrationAPI = ft.Button(content="Departure", color= "#D7E7F7", bgcolor= "#154275", on_click=lambda e: page.show_dialog(d))
    Duration2 = ft.Button(content="Return", color= "#D7E7F7", bgcolor= "#154275", on_click=lambda e: page.show_dialog(de), visible=False)
    Reset2= ft.Button(content="Reset", color= "#D7E7F7", bgcolor= "#154275", on_click=resett, visible=False)
        
    column2 = ft.Column(
        controls=[
            Plan, PlanAPI,
            ft.Container(height=50),
            Durration, DurrationAPI, Duration2,Reset2,
            ft.Container(height=50),
        ]
    )
        
        #3
    Depart = ft.Text(value="Departure Date", size = 30, color="#12366b")
    DepartAPI = ft.Text(value="", size = 20, color= "#000000")
 
    Arrive = ft.Text(value="Return Date", size = 30, color="#12366b")
    ArriveAPI = ft.Text(value="", size = 20, color= "#000000")
 
    column3 = ft.Column(
        controls=[
            Depart, DepartAPI,
            ft.Container(height=50),
            Arrive, ArriveAPI
        ]
    )
        
    Notes = ft.Text(value="Notes", size = 30, color="#12366b")
    NotesAPI = ft.TextField(label="Any more details", color= "#000000", multiline= True, max_length= 750, width=225, text_size=12, on_submit=SaveNotes)
 
    column4 = ft.Column(
            controls=[
                Notes, NotesAPI,
                ft.Container(height=50),
            ],
            alignment=ft.MainAxisAlignment.START
 
        )
 
    wContainer = ft.Container(content=ft.Row(
                controls=[column1, divide, column4, column2, column3], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                height=525,
                width = 1250,
                bgcolor="#FFFFFF",
                border_radius=10,
                padding=50,align=ft.Alignment.BOTTOM_CENTER)
 
    Third_Page = page.add(wContainer, Options2)
 
 
 
ft.run(main, assets_dir="assets")    
 
 
 