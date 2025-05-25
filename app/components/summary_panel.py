import flet as ft

class TopSummaryPanel(ft.Container):
    def __init__(self, page: ft.Page, label_refs):
        super().__init__(
            padding=10,
            bgcolor=ft.Colors.BLUE_GREY_800,
            expand=True,
            content=ft.Row(
                expand=True,
                scroll=ft.ScrollMode.AUTO,
                controls=[
                    ft.Column(
                        width=800,
                        height=150,
                        controls=[
                            # Primeira linha: Data, Tick, Rank, Fama, Pontuação
                            ft.Row(
                                controls=[
                                    ft.Text(ref=label_refs["horario"], size=12, width=180, color=ft.Colors.WHITE),
                                    ft.Text(ref=label_refs["tick"], size=12, width=120, color=ft.Colors.WHITE),
                                    ft.Text("Rank: 999999", size=12, width=140, color=ft.Colors.WHITE),
                                    ft.Text("Fama: 0", size=12, width=100, color=ft.Colors.WHITE),
                                    ft.Text("Pontuação: 0", size=12, width=140, color=ft.Colors.WHITE),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                            ),

                            # Segunda linha: Recursos
                            ft.Row(
                                controls=[
                                    ft.Text(ref=label_refs["metal"], size=12, width=175, color=ft.Colors.GREY_200),
                                    ft.Text(ref=label_refs["cristal"], size=12, width=175, color=ft.Colors.GREY_200),
                                    ft.Text(ref=label_refs["prometium"], size=12, width=175, color=ft.Colors.GREY_200),
                                    ft.Text(ref=label_refs["energia"], size=12, width=175, color=ft.Colors.GREY_200),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                            ),

                            # Terceira linha: Ícones de atalhos rápidos
                            ft.Row(
                                controls=[
                                    ft.Icon(name=ft.Icons.NEWSPAPER, color=ft.Colors.AMBER, tooltip="Notícias"),
                                    ft.Icon(name=ft.Icons.EMAIL, color=ft.Colors.ORANGE, tooltip="Mensagens"),
                                    ft.Icon(name=ft.Icons.FORUM, color=ft.Colors.AMBER, tooltip="Fórum"),
                                    ft.Icon(name=ft.Icons.WARNING, color=ft.Colors.RED, tooltip="Recebendo ataque"),
                                    ft.Icon(name=ft.Icons.SHIELD, color=ft.Colors.GREEN, tooltip="Recebendo defesa"),
                                    ft.Icon(name=ft.Icons.PUBLIC, color=ft.Colors.AMBER, tooltip="Tráfego em órbita"),
                                    ft.Icon(name=ft.Icons.CAMPAIGN, color=ft.Colors.BLUE, tooltip="Comunicados"),
                                    ft.Icon(name=ft.Icons.HELP, color=ft.Colors.BLUE, tooltip="Suporte"),
                                ],
                                spacing=65,
                                alignment=ft.MainAxisAlignment.CENTER
                            )
                        ],
                        spacing=30
                    )
                ]
            )
        )
