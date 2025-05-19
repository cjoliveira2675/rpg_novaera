import flet as ft
from app.components.header_info_panel import HeaderInfoPanel
from app.components.summary_panel import TopSummaryPanel
from app.state.shared_state import label_refs
from app.components.side_menu import SideMenu


class AppLayout(ft.Column):
    def __init__(self, page: ft.Page, nav_service, on_navigate):
        self.page = page
        self.nav_service = nav_service
        self.on_navigate = on_navigate

        super().__init__(
            expand=True,
            controls=[
                HeaderInfoPanel(),
                TopSummaryPanel(label_refs),
                ft.Row(
                    expand=True,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        # Menu lateral
                        ft.Container(
                            width=220,
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