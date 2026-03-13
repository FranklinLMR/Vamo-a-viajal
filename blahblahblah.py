import flet as ft 
import datetime
import subprocess
import os
import sys
import requests


SubRegRate= {
  "Northern Europe": 180,
  "Western Europe": 160,
  "Eastern Europe": 110,
  "Southern Europe": 140,

  "Northern Africa": 60,
  "Western Africa": 55,
  "Middle Africa": 70,
  "Eastern Africa": 65,
  "Southern Africa": 80,

  "Northern America": 210,
  "Central America": 95,
  "South America": 105,
  "Caribbean": 130,

  "Western Asia": 120,
  "Central Asia": 90,
  "Eastern Asia": 150,
  "Southern Asia": 85,
  "South-Eastern Asia": 100,

  "Australia and New Zealand": 190,
  "Melanesia": 120,
  "Micronesia": 110,
  "Polynesia": 130,

  "Antarctica": 350
}

def main(page: ft.Page):
    page.fonts = {
        "Main": "fredoka-latin-700-normal.ttf"
    }
    
    page.window.full_screen = True
    page.theme = ft.Theme(font_family="Main")
    page.title= "Via Py"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#f3f7ff"
    page.update()
    count= requests.get("https://restcountries.com/v3.1/all?fields=name,cca2")
    cdata =count.json()


    DataUser=["","","",""]
    Costs=0
    def mainmenu(e):
        secondpath= os.path.join(os.path.dirname(__file__), "main.py")
        subprocess.Popen(["python", secondpath])
        page.update()
        sys.exit(0)
        

    def SaveName(e):
        
        DataUser[0]=e.control.value

    def SaveNotes(e):
        DataUser[2]=e.control.value
    
    def SaveID(e):
        DataUser[1]=e.control.value

    
    def submitt(e):
        if DepartAPI.value and ArriveAPI.value != "":
            try:
                with open(f"{DataUser[1]}_Plan.txt", "w") as file:   #This is completely bad because it is better for sql
                    file.write(f"---User-Plan---\nName: {DataUser[0]}\nID or passport: {DataUser[1]}\nCountry: {DataUser[3]}\nDeparture Date: {DepartAPI.value}\nReturn Date: {ArriveAPI.value}\n{VisitsAPI.value}")
            except:
                for f in range(10):
                    print("Error, Missing data")
        else:
            for f in range(10):
                    print("Error, Missing data")

    def handle_change(e: ft.Event[ft.DateRangePicker]):
        global Costs
        DepartAPI.value = e.control.start_value.strftime('%m/%d/%Y')
        ArriveAPI.value = e.control.end_value.strftime('%m/%d/%Y')
        start = e.control.start_value   
        end = e.control.end_value   

        days= (end.date()- start.date()).days+1   #I got help from AI for this
        if DataUser[3] !="":
            inpt=DataUser[3].strip().split()
            namec = "%20".join(inpt)
            country = requests.get(f"https://restcountries.com/v3.1/name/{namec}?fullText=true&fields=name,capital,region,subregion,population,currencies,languages,flags,timezones,latlng,cca2,cca3,idd")


            if country.status_code == 200:
                Country_data= country.json()  
                subregion = Country_data[0].get("subregion") or ""
                rate = SubRegRate.get(subregion, 100)
                
                Costs= days*rate
                VisitsAPI.value = f"Number of days selected: {days}\nCost per night: USD${rate}\nTotal Cost: USD${Costs}"
                
            else:
                VisitsAPI.value = "Could not get country info."
        else:
            VisitsAPI.value = "Select a country first."
        page.update()
    

    def Drop(e):

        DepartAPI.value = ""
        ArriveAPI.value = ""
        VisitsAPI.value ="  "
        if DurrationAPI.on_click == None:
            DurrationAPI.on_click = lambda e: page.show_dialog(drp)
            DurrationAPI.bgcolor= "#154275"
            
        DataUser[3]=PlanAPI.value
        page.update()
        
        
    today = datetime.datetime.now()

    drp= ft.DateRangePicker(
        first_date=datetime.datetime(year=today.year, month=today.month, day=today.day+1),
        last_date=datetime.datetime(year=today.year, month=today.month+6, day=20),
        on_change=handle_change
    )
    Title = ft.Text("Book a flight! ", size=80, color="#12366b", align=ft.Alignment.CENTER, )

    Profile = ft.Container(ft.Image(src="profile.JPG"), width=200)
   
    Back= ft.Button(content="Main Menu", on_click= mainmenu)
    Submitts= ft.Button(content="Submit", on_click=submitt)


    PName = ft.Text(value="Full Name", size = 30, color="#12366b")
    NameAPI =ft.TextField(label="Insert your name", color= "#000000", max_length= 50, on_submit= SaveName)

    IDNumber = ft.Text(value="ID Number", size = 30, color="#12366b")
    IDAPI = ft.TextField(label="Insert your Passport or ID number",  color= "#000000", max_length=30, on_submit= SaveID)
    divide = ft.Container(bgcolor="#000000", height=500, width=2)

    column1 = ft.Column(controls=[ Profile,
        ft.Container(height=10),
        PName, NameAPI, 
        ft.Container(height=10),
        IDNumber, IDAPI,
        ft.Container(height=10),
        ], spacing=1, alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    
    #2

  


    Plan = ft.Text(value="Plan your trip", size = 30, color="#12366b")
    PlanAPI = ft.Dropdown(
        label="Select a country", editable= True,   
        width=200,
        options = [ft.dropdown.Option(key=c["name"]["common"], text=c["name"]["common"]) for c in cdata],
        on_select= Drop, text_style= ft.TextStyle( color="#516a8f" )
    )

    Durration = ft.Text(value="Set Duration", size = 20, color="#12366b")
    DurrationAPI = ft.Button(content="Departure", color= "#D7E7F7", bgcolor= "#939698", on_click=None)
    
    column2 = ft.Column(
    controls=[
        Plan, PlanAPI,
        ft.Container(height=50),
        Durration, DurrationAPI,
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
        Arrive, ArriveAPI,
        ft.Container(height=50),
    ]
)
    
    Notes = ft.Text(value="Notes", size = 30, color="#12366b")
    NotesAPI = ft.TextField(label="Any more details", color= "#000000", multiline= True, max_length= 750, width=225, text_size=12, on_submit=SaveNotes)

    Visits = ft.Text(value="Cost Estimation", size = 30, color="#12366b")
    VisitsAPI = ft.Text(value=f"", size = 20, color= "#000000")


    buttonVisits = ft.Button(content="Total Visit", 
                             width=100, 
                             height=50, 
                             bgcolor="#12366b", 
                             color="#FFFFFF", 
                             )

    column4 = ft.Column(
        controls=[
            Notes, NotesAPI,
            ft.Container(height=15),
            Visits, VisitsAPI,
            ft.Container(height=80),
        ft.Row(controls=[Back, Submitts])
        ],
        alignment=ft.MainAxisAlignment.START
    )

    wContainer = ft.Container(content=ft.Row(
            controls=[column1, divide, column2, column3, column4], alignment=ft.MainAxisAlignment.SPACE_EVENLY), 
            height=525, 
            width = 1250, 
            bgcolor="#FFFFFF", 
            border_radius=10,
            padding=50,align=ft.Alignment.BOTTOM_CENTER)
    
    #space
    space = ft.Container(height=10)
    
    #Main container
    blueCont = ft.Container(content=ft.Column(
        controls=[space, wContainer],
        spacing=20),
            height=700, 
            width = 1350, 
            bgcolor="#12366b",
            border_radius=10, align=ft.Alignment.BOTTOM_CENTER)
    
    Whole_page= ft.Column(controls=[Title, blueCont])

    page.add(Whole_page)
ft.run(main)