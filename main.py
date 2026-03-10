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
        # top= 100,
        # left= 600
        )

#logo image
    logo_image = ft.Image(
        src="Logo.png",
        visible= True,
        # top = 35,
        # right = 700,
        width= 700,
        height=400
    )

#buttons in main page

    #blueContainerfor real
    Button1 = ft.Button(content=ft.Text(value="Book a Flight!"), icon=ft.Icons.AIRPLANEMODE_ON, width=700, height=50)
    Button2 = ft.Button(content=ft.Text(value="Country Search"), icon=ft.Icons.MY_LOCATION,width=700, height=50)

    ColumnLeft = ft.Column(controls=[logo_image, Button1, Button2])
    ColumnRight = ft.Column(controls=[plane_image])

    Whole_page= ft.Row(controls=[ColumnLeft, ColumnRight])
    page.add(Whole_page)

    

ft.run(main, assets_dir="assets")    



