import flet as ft

class MarketPage:
    def __init__(self, page: ft.Page, on_navigate):
        self.page = page
        self.on_navigate = on_navigate

    def build(self):
        self.page.title = "RPG - Mercado"

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
                            ft.Text("Mercado...")
                        ]
                    )
                )
            ]
        )
