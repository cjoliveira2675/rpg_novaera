import flet as ft

def TopSummaryPanel():
    return ft.Container(
        padding=10,
        bgcolor=ft.colors.BLUE_GREY_800,
        height=150,
        content=ft.Column(
            controls=[
                # Primeira linha: Data, Tick, Rank, Fama, Pontuação
                ft.Row(
                    controls=[
                        ft.Text("Data/Hora do servidor: 01/05/2025 14:30", size=12, color=ft.colors.WHITE),
                        ft.Text("Tick atual: 12345", size=12, color=ft.colors.WHITE),
                        ft.Text("Rank: 42", size=12, color=ft.colors.WHITE),
                        ft.Text("Fama: 1342", size=12, color=ft.colors.WHITE),
                        ft.Text("Pontuação: 9800", size=12, color=ft.colors.WHITE),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),

                # Segunda linha: Recursos
                ft.Row(
                    controls=[
                        ft.Text("Metal: 12.300", size=12, color=ft.colors.GREY_200),
                        ft.Text("Cristal: 8.500", size=12, color=ft.colors.GREY_200),
                        ft.Text("Prometium: 3.700", size=12, color=ft.colors.GREY_200),
                        ft.Text("Energia: 15.000", size=12, color=ft.colors.GREY_200),
                        ft.Text("Fragmento estelar: 980", size=12, color=ft.colors.GREY_200),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),

                # Terceira linha: Ícones de atalhos rápidos
                ft.Row(
                    controls=[
                        ft.Icon(name=ft.icons.NEWSPAPER, color=ft.colors.AMBER, tooltip="Notícias"),
                        ft.Icon(name=ft.icons.EMAIL, color=ft.colors.ORANGE, tooltip="Mensagens"),
                        ft.Icon(name=ft.icons.FORUM, color=ft.colors.AMBER, tooltip="Fórum"),
                        ft.Icon(name=ft.icons.WARNING, color=ft.colors.RED, tooltip="Recebendo ataque"),
                        ft.Icon(name=ft.icons.SHIELD, color=ft.colors.GREEN, tooltip="Recebendo defesa"),
                        ft.Icon(name=ft.icons.PUBLIC, color=ft.colors.AMBER, tooltip="Tráfego em órbita"),
                        ft.Icon(name=ft.icons.CAMPAIGN, color=ft.colors.BLUE, tooltip="Comunicados"),
                        ft.Icon(name=ft.icons.HELP, color=ft.colors.BLUE, tooltip="Suporte"),
                    ],
                    spacing=20
                )
            ],
            spacing=10
        )
    )
