import flet as ft 

import requests

def main(page: ft.Page):
    page.fonts = {
        "Main": "fredoka-latin-700-normal.ttf"
    }
        
    page.theme = ft.Theme(font_family="Main")
    page.title= "Via Py"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#f3f7ff"
    page.update()

    Title = ft.Text("Book a flight! ", size=80, color="#12366b", align=ft.Alignment.CENTER, )

    Profile = ft.Container(ft.Image(src="profile.JPG"), width=200)

    PName = ft.Text(value="Full Name", size = 20, color="#12366b")
    NameAPI = ft.Text(value="Lorem Ipsum", size = 15, color= "#000000")

    IDNumber = ft.Text(value="ID Number", size = 20, color="#12366b")
    IDAPI = ft.Text(value="Lorem Ipsum", size = 15, color= "#000000")   

    divide = ft.Container(bgcolor="#000000", height=500, width=2)

    column1 = ft.Column(controls=[ Title,
        ft.Container(height=10),
        PName, NameAPI,
        ft.Container(height=10),
        IDNumber, IDAPI,
        ft.Container(height=10),
        ], spacing=1, alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    
    #2

    Plan = ft.Text(value="Plan your trip", size = 30, color="#12366b")
    PlanAPI = ft.Text(value="Lorem Ipsum", size = 20, color= "#000000")

    Durration = ft.Text(value="Duration", size = 20, color="#12366b")
    DurrationAPI = ft.Text(value="Lorem Ipsum", size = 15, color= "#000000")

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
    DepartAPI = ft.Text(value="Lorem Ipsum", size = 20, color= "#000000")

    Arrive = ft.Text(value="Arrival Date", size = 30, color="#12366b")
    ArriveAPI = ft.Text(value="Lorem Ipsum", size = 20, color= "#000000")

    column3 = ft.Column(
    controls=[
        Depart, DepartAPI,
        ft.Container(height=50),
        Arrive, ArriveAPI
    ]
)
    
    Notes = ft.Text(value="Notes", size = 30, color="#12366b")
    NotesAPI = ft.Text(value="Lorem Ipsum", size = 20, color= "#000000")

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

    page.add(wContainer, Profile)
ft.run(main, assets_dir="assets")