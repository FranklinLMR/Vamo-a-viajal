import flet as ft
import requests 


def main(page: ft.Page):
    
    page.title= "Truth or Dare"
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
        top = 100,
        right=600,
        width= 400
    )


    Whole_page= ft.Stack([plane_image, logo_image])
    page.add(Whole_page)

    

ft.run(main, assets_dir="assets")    



