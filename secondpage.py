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
    title = ft.Text("Country Search", size=80, color="#12366b")

#search bar

    search = ft.SearchBar(bar_hint_text="Search a Country...") 

#White container
    #collumn1
    #Flag = ft.Container(ft.Image(src=""))
    
    CName = ft.Text(value="Country Name", size = 20, color="#12366b")
    NameAPI = ft.Text(value="Lorem Ipsum", size = 15, color= "#000000")

    CapName = ft.Text(value="Capital City", size = 20, color="#12366b")
    CapAPI = ft.Text(value="Lorem Ipsum", size = 15, color= "#000000")

    Region = ft.Text(value="Region", size = 20, color="#12366b")
    RegAPI = ft.Text(value="Lorem Ipsum", size = 15, color= "#000000")

    SubRegion = ft.Text(value="Sub Region", size = 20, color="#12366b")
    SRegAPI = ft.Text(value="Lorem Ipsum", size = 15, color= "#000000")

    column1 = ft.Column(controls=[CName, NameAPI, CapName, CapAPI, Region, RegAPI, SubRegion, SRegAPI])

    #column2
    Popu = ft.Text(value="Population", size = 20, color="#12366b")
    PopuAPI = ft.Text(value="Lorem Ipsum", size = 15, color= "#000000")

    Curre = ft.Text(value="Currency", size = 20, color="#12366b")
    CurreAPI = ft.Text(value="Lorem Ipsum", size = 15, color= "#000000")

    Lan = ft.Text(value="Language", size = 20, color="#12366b")
    LanAPI = ft.Text(value="Lorem Ipsum", size = 15, color= "#000000")

    column2 = ft.Column(controls=[Popu, PopuAPI, Curre, CurreAPI, Lan, LanAPI])

    #column3
    Visa = ft.Text(value="Basic Visa", size = 20, color="#12366b")
    VisaAPI = ft.Text(value="Lorem Ipsum", size = 15, color= "#000000")

    cCode = ft.Text(value="Country Code", size = 20, color="#12366b")
    CCodeAPI = ft.Text(value="Lorem Ipsum", size = 15, color= "#000000")

    column3 = ft.Column(controls=[Visa, VisaAPI, cCode, CCodeAPI])

    #column4 I forgot to add it. (Im so done teacher)
    
    #White container
    wContainer = ft.Container(content=ft.Row(
            controls=[column1, column2, column3], alignment=ft.MainAxisAlignment.SPACE_EVENLY), 
            height=600, 
            width = 1200, 
            bgcolor="#FFFFFF", 
            border_radius=10,
            padding=50)
    
    #found documentation for the space_evenly im so lost with this new version
    
    #Main container
    blueCont = ft.Container(content=ft.Column(
        controls=[search, wContainer],
        spacing=20),
            height=700, 
            width = 1350, 
            bgcolor="#12366b",
            border_radius=10)
    
    Whole_page= ft.Column(controls=[title, blueCont])
    page.add(Whole_page)


ft.run(main, assets_dir="assets")    



