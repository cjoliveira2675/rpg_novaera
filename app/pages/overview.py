# app/ui/visao_geral_page.py

import flet as ft
from app.components.side_menu import SideMenu
from app.components.header_info_panel import HeaderInfoPanel
from app.components.summary_panel import TopSummaryPanel

class OverviewPage:
    def __init__(self, page: ft.Page, on_navigate):
        self.page = page
        self.on_navigate = on_navigate

    def build(self):
        self.page.controls.clear()
        self.page.title = "RPG - Visão Geral"

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
                            ft.Container(
                                expand=True,
                                content=ft.Column(
                                    scroll=ft.ScrollMode.AUTO,
                                    spacing=15,
                                    controls=[
                                        self.build_event_banner(),
                                        self.build_fleet_panel(),
                                        self.build_construction_queue(),
                                        self.build_research_queue(),
                                        self.build_production_queue(),
                                    ]
                                )

                            )
                            
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


    def build_event_banner(self):
        # Placeholder do banner deslizante
        return ft.Container(
            height=40,
            bgcolor=ft.colors.AMBER,
            border_radius=5,
            padding=10,
            content=ft.Text("[Banner de eventos/promos aqui - rotativo]", weight="bold")
        )

    def build_fleet_panel(self):
        # Placeholder para visualização de frotas em movimento
        return ft.Container(
            padding=10,
            bgcolor=ft.colors.BLUE_GREY_900,
            border_radius=5,
            content=ft.Column([
                ft.Text("Frotas em movimento (mock)", size=14, weight="bold", color=ft.colors.WHITE),
                ft.Text("Linha do tempo por ticks com setas -> ou <- conforme sentido", size=12, color=ft.colors.GREY_300),
            ])
        )

    def build_construction_queue(self):
        return ft.Container(
            padding=10,
            bgcolor=ft.colors.BLUE_GREY_800,
            border_radius=5,
            content=ft.Column([
                ft.Text("Construções em andamento e fila", size=14, weight="bold", color=ft.colors.WHITE),
            ])
        )

    def build_research_queue(self):
        return ft.Container(
            padding=10,
            bgcolor=ft.colors.BLUE_GREY_800,
            border_radius=5,
            content=ft.Column([
                ft.Text("Pesquisas em andamento e fila", size=14, weight="bold", color=ft.colors.WHITE),
            ])
        )

    def build_production_queue(self):
        return ft.Container(
            padding=10,
            bgcolor=ft.colors.BLUE_GREY_800,
            border_radius=5,
            content=ft.Column([
                ft.Text("Fila de produção (naves, canhões, escudos, etc)", size=14, weight="bold", color=ft.colors.WHITE),
            ])
        )