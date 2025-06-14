import flet as ft

class AlliancesPage:
    def __init__(self, page: ft.Page, on_navigate, game_manager=None, planeta=None):
        self.page = page
        self.on_navigate = on_navigate
        self.game_manager = game_manager
        self.planeta = planeta

    def build(self):
        self.page.title = "RPG - Aliança"

        return ft.Column(
            expand=True,
            controls=[
                #TopSummaryPanel(label_refs),
                ft.Container(
                    expand=True,
                    content=ft.Column(
                        scroll=ft.ScrollMode.AUTO,
                        spacing=15,
                        controls=[
                            ft.Text("Aliança...")
                        ]
                    )
                )
            ]
        )