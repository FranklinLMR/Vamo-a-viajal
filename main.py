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

    page.bgcolor = "#f3f7ff"
    page.expand=True
    page.update()

#main page image
    plane_image= ft.Image(
        src="Plane2.jpg", 
        visible=True, 
        width=635,
        height=544.5,
        scale= 1.55 ,
        expand=True
        
        )

#logo image
    logo_image = ft.Image(
        src="Logo.png",
        visible= True,
        # top = 35,
        # right = 700,
        width= 700,
        height=400,
        scale=0.8
    )

#buttons in main page

    #blueContainerfor real
    Button1 = ft.Button(content=ft.Text(value="Book a Flight!"), icon=ft.Icons.AIRPLANEMODE_ON, width=700, height=50)
    Button2 = ft.Button(content=ft.Text(value="Country Search"), icon=ft.Icons.MY_LOCATION,width=700, height=50)

    ColumnLeft = ft.Column(controls=[logo_image, Button1, Button2]
    )
    ColumnRight = ft.Column(controls=[plane_image],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    Whole_page= ft.Row(controls=[ColumnLeft, ColumnRight],spacing=180, expand= True)
    page.add(Whole_page)

    

ft.run(main, assets_dir="assets")    



