# app/navigation/navigation_service.py

import flet as ft

from app.pages.overview import OverviewPage
from app.pages.notifications import NotificationsPage
from app.pages.messages import MessagesPage
from app.pages.announcements import AnnouncementsPage
from app.pages.resources import ResourcesPage
from app.pages.research_lab import ResearchLabPage
from app.pages.buildings import BuildingsPage
from app.pages.hangar import HangarPage
from app.pages.sdp import SDPPage
from app.pages.command_core import CommandCorePage
from app.pages.fleets import FleetsPage
from app.pages.observatory import ObservatoryPage
from app.pages.traffic import TrafficPage
from app.pages.archives import ArchivesPage
from app.pages.battle_logs import BattleLogsPage
from app.pages.simulators import SimulatorsPage
from app.pages.rankings import RankingsPage
from app.pages.advanced_buildings import AdvancedBuildingsPage
from app.pages.gates import GatesPage
from app.pages.e_m_e import EMEPage
from app.pages.star_cannon import StarCannonPage
from app.pages.moons import MoonsPage
from app.pages.community import CommunityPage
from app.pages.market import MarketPage
from app.pages.alliances import AlliancesPage
from app.pages.store import StorePage
from app.pages.cosmic_events import CosmicEventsPage
from app.pages.expeditions import ExpeditionsPage


class NavigationService:
    def __init__(self, page: ft.Page):
        self.page = page
        self.routes = [
            OverviewPage,
            NotificationsPage,
            MessagesPage,
            AnnouncementsPage,
            ResourcesPage,
            ResearchLabPage,
            BuildingsPage,
            HangarPage,
            SDPPage,
            CommandCorePage,
            FleetsPage,
            ObservatoryPage,
            TrafficPage,
            ArchivesPage,
            BattleLogsPage,
            SimulatorsPage,
            RankingsPage,
            AdvancedBuildingsPage,
            GatesPage,
            EMEPage,
            StarCannonPage,
            MoonsPage,
            CommunityPage,
            MarketPage,
            AlliancesPage,
            StorePage,
            CosmicEventsPage,
            ExpeditionsPage,
        ]

    def navigate_to(self, index: int):
        if index < 0 or index >= len(self.routes):
            print(f"Índice de navegação inválido: {index}")
            return
        self.page.clean()
        page_class = self.routes[index]
        self.page.add(page_class(self.page, self.navigate_to).build())
