import flet as ft
import asyncio
from datetime import datetime
from app.navigation.navigation_service import NavigationService
from app.layout.app_layout import AppLayout 
from app.state.shared_state import label_refs, tick_counter

from app.components.summary_panel import TopSummaryPanel

from core.controllers.game_manager import GameManager
from core.models.planeta import Planeta
from core.models.jogador import Jogador


async def main(page: ft.Page):
    # Configurações
    page.title = "RPG Nova Era"
    page.theme_mode = ft.ThemeMode.DARK

    jogador = Jogador()
    planeta = Planeta()
    top_summary = TopSummaryPanel()
    manager = GameManager(jogador, planeta, top_summary=top_summary, page=page)

    # Setup
    nav_service = NavigationService(
        page,
        jogador=jogador,
        planeta=planeta,
        game_manager=manager
    )

    def on_navigate(index):
        nav_service.navigate_to(index)

    layout = AppLayout(page, nav_service, on_navigate, top_summary=top_summary)
    page.add(layout)

    # ESPERE UM POUCO antes de chamar navigate_to(0)
    await asyncio.sleep(0.1)
    nav_service.navigate_to(0)

    asyncio.create_task(manager.iniciar_tick_loop())

ft.app(target=main, view=ft.WEB_BROWSER)