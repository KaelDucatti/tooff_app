import flet as ft
from pages.login_page import login_page


def main(page: ft.Page):
    login_page(page)


ft.app(target=main)
