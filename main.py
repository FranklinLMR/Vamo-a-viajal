import flet as ft
import requests 
import os
import subprocess


def main(page: ft.Page):
    

    def secondpage(e):
        secondpath= os.path.join(os.path.dirname(__file__), "secondpage.py")
        subprocess.Popen(["python", secondpath])
        page.window.close()
        
    #fonts
    page.fonts = {
        "Main": "fredoka-latin-700-normal.ttf"
    }

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
    ButtonA= ft.Container(on_click= secondpage, content=ft.Image(src="Tripbutton.png"),scale=2, ink= True, width=300, height=60, margin=40, border_radius=100)
    ButtonB= ft.Container(on_click= secondpage, content=ft.Image(src="Countrybutton.png"),scale=2
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

    

ft.run(main, assets_dir="assets")    



