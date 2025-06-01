import flet as ft

class OverviewPage:
    def __init__(self, page: ft.Page, on_navigate, game_manager=None, planeta=None):
        self.page = page
        self.on_navigate = on_navigate
        self.game_manager = game_manager
        self.planeta = planeta

    def build(self):
        self.page.title = "RPG - Visão Geral"

        return ft.Row(
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Column(
                    width=820,
                    height=800,
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                        self.build_event_banner(),
                        self.build_fleet_panel(),
                        self.build_construction_queue(),
                        self.build_research_queue(),                    
                        self.build_production_queue()                        
                    ]
                )
            ]
        )

    def build_event_banner(self):
        return ft.Container(
            height=40,
            bgcolor=ft.Colors.AMBER,
            border_radius=5,
            padding=10,
            content=ft.Text("[Banner de eventos/promos aqui - rotativo]", weight="bold")
        )

    def build_fleet_panel(self):
        return ft.Container(
            padding=10,
            bgcolor=ft.Colors.BLUE_GREY_900,
            border_radius=5,
            content=ft.Column([
                ft.Text("Frotas em movimento (mock)", size=14, weight="bold", color=ft.Colors.WHITE),
                ft.Text("Linha do tempo por ticks com setas -> ou <- conforme sentido", size=12, color=ft.Colors.GREY_300),
            ])
        )

    def build_construction_queue(self):
        return ft.Container(
            padding=10,
            bgcolor=ft.Colors.BLUE_GREY_800,
            border_radius=5,
            content=ft.Column([
                ft.Text("Construções em andamento e fila.", size=14, weight="bold", color=ft.Colors.WHITE),
            ])
        )

    def build_research_queue(self):
        return ft.Container(
            padding=10,
            bgcolor=ft.Colors.BLUE_GREY_800,
            border_radius=5,
            content=ft.Column([
                ft.Text("Pesquisas em andamento e fila", size=14, weight="bold", color=ft.Colors.WHITE),
            ])
        )

    def build_production_queue(self):
        return ft.Container(
            padding=10,
            bgcolor=ft.Colors.BLUE_GREY_800,
            border_radius=5,
            content=ft.Column([
                ft.Text("Fila de produção (naves, canhões, escudos, etc)", size=14, weight="bold", color=ft.Colors.WHITE),
            ])
        )