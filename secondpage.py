import flet as ft
import requests 


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
    NameAPI = ft.Text(value="Lorem Ipsum", size = 15, color= "#000000")

    CapName = ft.Text(value="Capital City", size = 20, color="#12366b")
    CapAPI = ft.Text(value="Lorem Ipsum", size = 15, color= "#000000")

    Region = ft.Text(value="Region", size = 20, color="#12366b")
    RegAPI = ft.Text(value="Lorem Ipsum", size = 15, color= "#000000")

    SubRegion = ft.Text(value="Sub Region", size = 20, color="#12366b")
    SRegAPI = ft.Text(value="Lorem Ipsum", size = 15, color= "#000000")


    column1 = ft.Column(controls=[ Flag,
        ft.Container(height=20),
        CName, NameAPI,
        ft.Container(height=20),
        CapName, CapAPI,
        ft.Container(height=20),
        Region, RegAPI,
        ft.Container(height=20),
        SubRegion, SRegAPI], spacing=1, alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    
#I know I can do it another way but like this is easier for me to then change the value of the lorem ipsum part ;)

    #column2
    Popu = ft.Text(value="Population", size = 30, color="#12366b")
    PopuAPI = ft.Text(value="Lorem Ipsum", size = 20, color= "#000000")

    Curre = ft.Text(value="Currency", size = 30, color="#12366b")
    CurreAPI = ft.Text(value="Lorem Ipsum", size = 20, color= "#000000")

    Lan = ft.Text(value="Language", size = 30, color="#12366b")
    LanAPI = ft.Text(value="Lorem Ipsum", size = 20, color= "#000000")

    column2 = ft.Column(
    controls=[
        Popu,PopuAPI,
        ft.Container(height=25),
        Curre, CurreAPI,
        ft.Container(height=25),
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
        ft.Container(height=25),
        cCode,
        CCodeAPI
    ]
)

    #column4 I forgot to add it. (Im so done teacher)
    Tzone = ft.Text(value="Time Zone", size = 30, color="#12366b")
    TZoneAPI = ft.Text(value="Lorem Ipsum", size = 20, color= "#000000")

    Weather = ft.Text(value="Weather", size = 30, color="#12366b")
    WeatherAPI = ft.Text(value="Lorem Ipsum", size = 20, color= "#000000")

    LocTime = ft.Text(value="Local Time", size = 30, color="#12366b")
    LocTimeAPI = ft.Text(value="Lorem Ipsum", size = 20, color= "#000000")

    column4 = ft.Column(
        controls=[
            Tzone, TZoneAPI,
            ft.Container(height=15),
            Weather, WeatherAPI,
            ft.Container(height=15),
            LocTime, LocTimeAPI
        ],
        alignment=ft.MainAxisAlignment.START
    )    
    #White container
    wContainer = ft.Container(content=ft.Row(
            controls=[column1, column4, column2, column3], alignment=ft.MainAxisAlignment.SPACE_EVENLY), 
            height=500, 
            width = 1200, 
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



