import flet as ft
from app.navigation.navigation_service import NavigationService
from app.components.side_menu import SideMenu

def main(page: ft.Page):
    page.title = "RPG Nova Era - Universo sem fronteiras"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.window_width = 1200
    page.window_height = 700
    page.window_resizable = True

    nav_service = NavigationService(page)

    def on_navigate(index):
        nav_service.navigate_to(index)

    # Monta o menu lateral
    side_menu = SideMenu(page, on_navigate)

    # Layout com o menu à esquerda e conteúdo à direita
    layout = ft.Row(
        [
            ft.Container(side_menu, width=200, bgcolor=ft.Colors.BLUE_GREY_900),  # tom escuro e elegante
            ft.Container(expand=True)  # Onde as páginas serão carregadas
        ],
        expand=True
    )

    page.add(layout)
    nav_service.navigate_to(0)  # Visão geral como página inicial

if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)
