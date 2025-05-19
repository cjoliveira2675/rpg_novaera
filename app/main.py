import flet as ft
import asyncio
from datetime import datetime
from app.navigation.navigation_service import NavigationService
from app.components.side_menu import SideMenu
from app.layout.app_layout import AppLayout 
from app.state.shared_state import label_refs, tick_counter

from core.controllers.game_manager import GameManager
from core.models.recursos import Recursos
from core.models.constructions_model import MinaMetal, PlantaSolar
from core.models.tecnologias_model import MineracaoAvancada


class Jogador:
    def __init__(self):
        self.tecnologias = [MineracaoAvancada(pesquisada=True)]

class Planeta:
    def __init__(self):
        self.nome = "Éden Prime"
        self.recursos = Recursos(metal=2500, cristal=1000, prometium=0, energia=100)
        self.construcoes = [
            MinaMetal(nivel=1, construido=True),
            PlantaSolar(nivel=1, construido=True)
        ]


async def main(page: ft.Page):
    # Configurações
    page.title = "RPG Nova Era"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 1200
    page.window_height = 700

    # Setup
    nav_service = NavigationService(page)

    def on_navigate(index):
        nav_service.navigate_to(index)

    layout = AppLayout(page, nav_service, on_navigate)

    page.add(layout)

    # ESPERE UM POUCO antes de chamar navigate_to(0)
    await asyncio.sleep(0.1)
    nav_service.navigate_to(0)

    jogador = Jogador()
    planeta = Planeta()
    manager = GameManager(jogador, planeta)

    async def tick_loop():
        while True:
            manager.processar_tick()
            tick_counter["value"] += 1

            # Atualizar hora e tick
            label_refs["horario"].current.value = f"Servidor: {datetime.now().strftime('%d/%m/%Y %H:%M')}"
            label_refs["tick"].current.value = f"Tick atual: {tick_counter['value']}"
            # Atualizar recursos
            label_refs["metal"].current.value = f"Metal: {planeta.recursos.metal}"
            label_refs["cristal"].current.value = f"Cristal: {planeta.recursos.cristal}"
            label_refs["prometium"].current.value = f"Prometium: {planeta.recursos.prometium}"
            label_refs["energia"].current.value = f"Energia: {planeta.recursos.energia}"

            page.update()
            await asyncio.sleep(3)

    asyncio.create_task(tick_loop())

ft.app(target=main, view=ft.WEB_BROWSER)