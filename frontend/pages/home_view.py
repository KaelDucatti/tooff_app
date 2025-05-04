import flet as ft


def home_view(page: ft.Page):
    page.views.clear()
    page.views.append(
        ft.View(
            "/home",
            [
                ft.AppBar(title=ft.Text("Página Inicial")),
                ft.Text("Você está na página inicial!", size=24),
            ],
        )
    )
    page.update()
