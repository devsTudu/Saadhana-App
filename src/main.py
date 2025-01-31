import flet as ft
from models.saadhana import HabitCard
from models.elements import myAppBar


def main(page: ft.Page):
    page.title = "Saadhana App"
    top_bar = myAppBar("Debasish")
    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                ft.View("/",
                        [   
                            top_bar,
                            ft.ListView(
                                [
                                    HabitCard("Hello","Boss this is the detail"),
                                    HabitCard("Sleeping", "Sleeping on time")]),
                            ft.ElevatedButton("Go somewhere",on_click=lambda _: page.go("/some"))
                        ])
            )
        elif page.route == "/some":
            page.views.append(
                ft.View(
                    "/some",
                    [
                        ft.Text("Welcome to somewhere"),
                        ft.Button("Go Home",on_click=lambda _:page.go("/"))
                    ]
                    
                )
            )
        page.update()
        
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
        
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(main)
