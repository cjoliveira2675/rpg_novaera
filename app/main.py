import flet as ft
from app.ui.home import HomePage

def main(page: ft.Page):
    page.title = "RPG Nova Era - Universo sem fronteiras"
    home = HomePage(page)
    home.build()
    page.update()

if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)
