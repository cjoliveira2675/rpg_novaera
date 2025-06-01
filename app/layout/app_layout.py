import flet as ft
from app.components.header_info_panel import HeaderInfoPanel
from app.components.summary_panel import TopSummaryPanel
from app.components.side_menu import SideMenu


class AppLayout(ft.Column):
    def __init__(self, page: ft.Page, nav_service, on_navigate, top_summary: TopSummaryPanel):
        self.page = page
        self.nav_service = nav_service
        self.on_navigate = on_navigate
        self.top_summary = top_summary

        super().__init__(
            expand=True,
            controls=[
                ft.Row(
                    width=1060,
                    height=150,
                    controls=[
                        ft.Container(
                            content=HeaderInfoPanel()
                        ),
                        
                        ft.Container(
                            expand=True,
                            content=top_summary
                        )
                    ]
                ),
                ft.Row(
                    expand=True,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        # Menu lateral
                        ft.Container(
                            width=220,
                            height=800,
                            bgcolor=ft.Colors.BLUE_GREY_900,
                            content=SideMenu(self.page, self.on_navigate)
                        ),

                        # Área de conteúdo dinâmica
                        ft.Container(
                            expand=True,
                            padding=10,
                            ref=self.nav_service.content_ref  # <- definido no NavigationService
                        )
                    ]
                )
            ]
        )