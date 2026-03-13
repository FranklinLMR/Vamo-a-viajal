import flet as ft 
import datetime
import requests
import subprocess
import os 
import sys


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
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.update()

    DataUser=["","","",""]
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

    page.add(wContainer, Options2)
ft.run(main, assets_dir="assets")