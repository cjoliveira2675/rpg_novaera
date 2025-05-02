# app/navigation/navigation_service.py

import flet as ft
from app.pages.overview import OverviewPage
from app.pages.resources import ResourcesPage
from app.pages.research_lab import ResearchLabPage
from app.pages.buildings import BuildingsPage
from app.pages.notifications import NotificationsPage

class NavigationService:
    def __init__(self, page: ft.Page):
        self.page = page
        self.routes = [
            OverviewPage,
            ResourcesPage,
            ResearchLabPage,
            BuildingsPage,
            NotificationsPage,
        ]
        self.nav_rail = None

    def build_menu(self, on_navigate):
        self.nav_rail = ft.NavigationRail(
            destinations=[
                ft.NavigationRailDestination(icon=ft.icons.HOME, label="Visão Geral"),
                ft.NavigationRailDestination(icon=ft.icons.STORAGE, label="Recursos"),
                ft.NavigationRailDestination(icon=ft.icons.SCIENCE, label="Pesquisas"),
                ft.NavigationRailDestination(icon=ft.icons.LOCATION_CITY, label="Construções"),
                ft.NavigationRailDestination(icon=ft.icons.NOTIFICATIONS, label="Notificações"),
            ],
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            on_change=lambda e: on_navigate(e.control.selected_index),
        )
        return self.nav_rail

    def navigate_to(self, index):
        self.page.clean()  # Limpa os controles da tela
        page_class = self.routes[index]
        self.page.add(page_class(self.page, self.navigate_to).build())

