# app/components/side_menu.py

import flet as ft

class SideMenu(ft.Container):
    def __init__(self, page: ft.Page, on_navigate):
        super().__init__(
            width=220,
            bgcolor=ft.colors.BLUE_GREY_900,
            padding=20,
            content=ft.Column(
                controls=[
                    ft.Text("Navegação", size=16, weight="bold", color=ft.colors.WHITE),
                    ft.Divider(color=ft.colors.WHITE),
                    ft.ElevatedButton("Visão Geral", on_click=lambda _: on_navigate(0)),
                    ft.ElevatedButton("Recursos", on_click=lambda _: on_navigate(1)),
                    ft.ElevatedButton("Laboratório", on_click=lambda _: on_navigate(2)),
                    ft.ElevatedButton("Construções", on_click=lambda _: on_navigate(3)),
                    ft.ElevatedButton("Notificações", on_click=lambda _: on_navigate(4)),
                ],
                spacing=10
            )
        )
