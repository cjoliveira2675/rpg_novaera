import flet as ft

class ResourcesPage:
    def __init__(self, page: ft.Page, on_navigate, game_manager=None, planeta=None):
        self.page = page
        self.on_navigate = on_navigate
        self.game_manager = game_manager
        self.planeta = planeta

        # Reutiliza as construções já instanciadas no planeta
        self.mina_metal = self.planeta.mina_metal
        self.mina_cristal = self.planeta.mina_cristal
        self.planta_solar = self.planeta.planta_solar
        self.armazem_metal = self.planeta.armazem_metal
        self.armazem_cristal = self.planeta.armazem_cristal

    def build(self):
        self.page.title = "RPG - Recursos"

        return ft.Column(
            expand=True,
            controls=[
                ft.Container(
                    expand=True,
                    padding=10,
                    content=ft.Column(
                        spacing=10,
                        controls=[
                            ft.Row(
                                spacing=15,
                                controls=[
                                    self.build_construcao_painel("Mina de Metal", self.mina_metal),
                                    self.build_construcao_painel("Mina de Cristal", self.mina_cristal),
                                    self.build_construcao_painel("Planta Solar", self.planta_solar),
                                ]
                            ),
                            ft.Row(
                                spacing=15,
                                controls=[
                                    self.build_construcao_painel("Armazém Metal", self.armazem_metal),
                                    self.build_construcao_painel("Armazém Cristal", self.armazem_cristal),
                                ]
                            )
                        ]
                    )
                )
            ]
        )

    def build_construcao_painel(self, nome, construcao):
        label_nivel = ft.Text(f"Nível: {construcao.nivel}", size=12)

        return ft.Container(
            height=105,
            bgcolor=ft.Colors.BLUE_GREY_900,
            padding=10,
            border_radius=5,
            content=ft.Column([
                ft.Text(nome, size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.AMBER),
                label_nivel,
                ft.ElevatedButton(
                    text="Evoluir" if construcao.construido else "Construir",
                    icon=ft.Icons.UPGRADE,
                    on_click=lambda e: self.game_manager.executar_acao(construcao, label_nivel)
                )
            ])
        )