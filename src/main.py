import flet as ft
from flet.auth import OAuthProvider
from models.saadhana import HabitCard
from models.elements import myAppBar
from pages import main_page,new_habit

def main(page: ft.Page):
    page.title = "Saadhana App"
    top_bar = myAppBar("Debasish")
    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                main_page.view_homepage(page)
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
        
        elif page.route == "/new":
            page.views.append(
                new_habit.view(page)
                )
        
        page.update()
        
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
        
    def google_authenticate(e):
        # Implement Google authentication logic here
        
        page.snack_bar = ft.SnackBar(ft.Text("Authenticated with Google"))
        page.snack_bar.open = True
        page.update()
        
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(main)
