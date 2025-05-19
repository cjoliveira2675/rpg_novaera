import flet as ft

class HeaderInfoPanel(ft.Container):
    def __init__(self):
        super().__init__(
            padding=10,
            bgcolor=ft.Colors.BLUE_GREY_900,
            height=150,
            content=ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Image(
                        src="https://cdn-icons-png.flaticon.com/512/616/616408.png",
                        width=60,
                        height=60,
                        fit=ft.ImageFit.CONTAIN
                    ),
                    ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=2,
                        controls=[
                            ft.Text("Junior da Terra", size=16, weight="bold", color=ft.Colors.WHITE),
                            ft.Text("[1:5:3:9:2]", size=12, color=ft.Colors.GREY_300),
                            ft.Text("Raça: Humanos", size=12, color=ft.Colors.GREY_200),
                        ]
                    )
                ]
            )
        )
