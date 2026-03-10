import flet as ft
import datetime
import requests 


def main(page: ft.Page):
    
    page.title= "Truth or Dare"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#f3f7ff"
    page.update()


    today = datetime.datetime.now()


    d = ft.DatePicker(
        first_date=datetime.datetime(year=today.year, month=today.month, day=today.day+1),
        last_date=datetime.datetime(year=today.year + 1, month=today.month, day=20))



    plane_image= ft.Image(
        src="assets/Plane.jpg", 
        visible=True, 
        top= 100,
        left= 600,
        width= 1080,
        height= 720
        )

    Whole_page= ft.Stack([plane_image])
    page.add(Whole_page)




ft.run(main, assets_dir="assets")    



