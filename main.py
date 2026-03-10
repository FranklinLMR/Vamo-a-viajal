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

#main page image
    plane_image= ft.Image(
        src="Plane.jpg", 
        visible=True, 
        top= 100,
        left= 600
        )

#logo image
    logo_image = ft.Image(
        src="Logo.png",
        visible= True,
        top = 35,
        right = 700,
        width= 700,
        height=400
    )

#buttons in main page
    #blueContainer
    blueButton = ft.Container(
        bgcolor="#003d99",
        height = 30,
        width = 600,
        border_radius=10
        )
    #whiteContainer
    whiteButton = ft.Container(
        bgcolor="#003d99",
        height = 30,
        width = 600,
        border_radius=10
        )
    #images
    canvaPlane = ft.Image(
        src="Plane.jpg",
        height = 25
    )
    #Text
    textButton1 = ft.Text(
        value="Book your flight!",
        color="#000000",
        size = 15
    )

    #stack for Book a flight
    BookaFLight = ft.Stack([blueButton,whiteButton,canvaPlane,textButton1])

    Whole_page= ft.Stack([plane_image, logo_image])
    page.add(Whole_page, BookaFLight)

    

ft.run(main, assets_dir="assets")    



