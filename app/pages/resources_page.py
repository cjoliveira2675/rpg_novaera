import flet as ft
from core.models.constructions_model import MinaMetal, MinaCristal, PlantaSolar
from core.controllers.game_manager import GameManager
from app.state.shared_state import label_refs
from core.models.jogador import Jogador
from core.models.planeta import Planeta

class ResourcesPage:
    def __init__(self, page: ft.Page, on_navigate):
        self.page = page
        self.on_navigate = on_navigate
        
        # Instâncias das construções
        self.mina_metal = MinaMetal(nivel=1, construido=True)
        self.mina_cristal = MinaCristal(nivel=1, construido=True)
        self.planta_solar = PlantaSolar(nivel=1, construido=True)

        self.planeta = Planeta(nome="Planeta Alpha", construcoes=[
            self.mina_metal, self.mina_cristal, self.planta_solar
        ])
        self.jogador = Jogador(nome="Jogador Teste", tecnologias=[])

        self.game_manager = GameManager(self.jogador, self.planeta)

    def build(self):
        self.page.title = "RPG - Recursos"

        return ft.Column(
            expand=True,
            controls=[
                ft.Container(
                    expand=True,
                    padding=10,
                    content=ft.Column(
                        scroll=ft.ScrollMode.AUTO,
                        spacing=15,
                        controls=[
                            self.build_construcao_painel("Mina de Metal", self.mina_metal),
                            self.build_construcao_painel("Mina de Cristal", self.mina_cristal),
                            self.build_construcao_painel("Planta Solar", self.planta_solar),
                        ]
                    )
                )
            ]
        )

    def build_construcao_painel(self, nome, construcao):
        label_nivel = ft.Text(f"Nível: {construcao.nivel}", size=12)

        return ft.Container(
            bgcolor=ft.Colors.BLUE_GREY_900,
            padding=10,
            border_radius=5,
            content=ft.Column([
                ft.Text(nome, size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.AMBER),
                label_nivel,
                ft.ElevatedButton(
                    text="Evoluir" if construcao.construido else "Construir",
                    icon=ft.Icons.UPGRADE,
                    on_click=lambda e: self.executar_acao(nome, construcao, label_nivel)
                )
            ])
        )

    def executar_acao(self, nome, construcao, label_nivel):
        # Simples chamada ao gerenciador do jogo (sem validações por enquanto)
        self.game_manager.evoluir_construcao(construcao)

        # Atualiza a interface com o novo nível
        label_nivel.value = f"Nível: {construcao.nivel}"
        self.page.update()