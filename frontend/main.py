import flet as ft
from frontend.pages.login_view import login_view
from frontend.pages.home_view import home_view


def main(page: ft.Page):
    def route_change(e):
        if page.route == "/":
            login_view(page)
        elif page.route == "/home":
            home_view(page)

    page.on_route_change = route_change
    page.go(page.route)


ft.app(target=main)
