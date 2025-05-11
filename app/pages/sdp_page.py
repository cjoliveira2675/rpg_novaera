# app/ui/visao_geral_page.py

import flet as ft
from app.components.side_menu import SideMenu
from app.components.header_info_panel import HeaderInfoPanel
from app.components.summary_panel import TopSummaryPanel

class SDPPage:
    def __init__(self, page: ft.Page, on_navigate):
        self.page = page
        self.on_navigate = on_navigate

    def build(self):
        self.page.controls.clear()
        self.page.title = "RPG - Sistema de defesa"

        return ft.Row(
            controls=[

                # Coluna da esquerda: HeaderInfoPanel em cima, SideMenu embaixo
                ft.Container(
                    width=220,
                    padding=ft.padding.only(top=10, right=0, bottom=10, left=10),
                    content=ft.Column(
                        controls=[
                            HeaderInfoPanel(),
                            SideMenu(self.page, self.on_navigate)
                        ],
                        spacing=10,  # define espaçamento interno controlado
                        expand=True,
                        alignment=ft.MainAxisAlignment.START,
                    )
                ),

                # Coluna central: TopSummaryPanel em cima, conteúdo abaixo
                ft.Container(
                    expand=True,
                    padding=ft.padding.only(top=10, right=10, bottom=10, left=0),
                    content=ft.Column(
                        controls=[
                            TopSummaryPanel(),
                            ft.Text("Conteúdo de SDP...")
                        ],
                        spacing=10,
                        expand=True,
                        alignment=ft.MainAxisAlignment.START,
                    )
                )
            ],
            expand=True,
            vertical_alignment=ft.CrossAxisAlignment.START
        )
