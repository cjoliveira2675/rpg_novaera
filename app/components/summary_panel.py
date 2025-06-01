import flet as ft

class TopSummaryPanel(ft.Container):
    def __init__(self):
        super().__init__(
            padding=10,
            bgcolor=ft.Colors.BLUE_GREY_800,
            expand=True
        )

        # Labels internos
        self.label_metal = ft.Text(size=12, width=175, color=ft.Colors.GREY_200)
        self.label_cristal = ft.Text(size=12, width=175, color=ft.Colors.GREY_200)
        self.label_prometium = ft.Text(size=12, width=175, color=ft.Colors.GREY_200)
        self.label_energia = ft.Text(size=12, width=175, color=ft.Colors.GREY_200)

        # Hora e tick permanecem via label_refs
        self.label_horario = ft.Text(size=12, width=180, color=ft.Colors.WHITE)
        self.label_tick = ft.Text(size=12, width=120, color=ft.Colors.WHITE)

        self.content = ft.Row(
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Column(
                    width=800,
                    height=150,
                    spacing=30,
                    controls=[
                        ft.Row(
                            controls=[
                                self.label_horario,
                                self.label_tick,
                                ft.Text("Rank: 999999", size=12, width=140, color=ft.Colors.WHITE),
                                ft.Text("Fama: 0", size=12, width=100, color=ft.Colors.WHITE),
                                ft.Text("Pontuação: 0", size=12, width=140, color=ft.Colors.WHITE),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        ft.Row(
                            controls=[
                                self.label_metal,
                                self.label_cristal,
                                self.label_prometium,
                                self.label_energia,
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
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
                    ]
                )
            ]
        )

    def atualizar(self, recursos, energia_liquida: int):
        self.label_metal.value = f"Metal: {recursos.metal}"
        self.label_cristal.value = f"Cristal: {recursos.cristal}"
        self.label_prometium.value = f"Prometium: {recursos.prometium}"

        cor = ft.Colors.GREEN if energia_liquida >= 0 else ft.Colors.RED
        self.label_energia.value = f"⚡ Energia: {energia_liquida}"
        self.label_energia.color = cor

    def atualizar_tempo_e_tick(self, horario: str, tick: int):
        self.label_horario.value = f"Servidor: {horario}"
        self.label_tick.value = f"Tick atual: {tick}"