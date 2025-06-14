# app/navigation/navigation_service.py

import flet as ft

from app.pages.overview_page import OverviewPage
from app.pages.notifications_page import NotificationsPage
from app.pages.messages_page import MessagesPage
from app.pages.announcements_page import AnnouncementsPage
from app.pages.resources_page import ResourcesPage
from app.pages.research_lab_page import ResearchLabPage
from app.pages.buildings_page import BuildingsPage
from app.pages.hangar_page import HangarPage
from app.pages.sdp_page import SDPPage
from app.pages.command_core_page import CommandCorePage
from app.pages.fleets_page import FleetsPage
from app.pages.observatory_page import ObservatoryPage
from app.pages.traffic_page import TrafficPage
from app.pages.archives_page import ArchivesPage
from app.pages.battle_logs_page import BattleLogsPage
from app.pages.simulators_page import SimulatorsPage
from app.pages.rankings_page import RankingsPage
from app.pages.advanced_buildings_page import AdvancedBuildingsPage
#from app.pages.gates_page import GatesPage
#from app.pages.e_m_e_page import EMEPage
#from app.pages.star_cannon_page import StarCannonPage
from app.pages.moons_page import MoonsPage
from app.pages.community_page import CommunityPage
from app.pages.market_page import MarketPage
from app.pages.alliances_page import AlliancesPage
from app.pages.store_page import StorePage
from app.pages.cosmic_events_page import CosmicEventsPage
from app.pages.expeditions_page import ExpeditionsPage


class NavigationService:
    def __init__(self, page: ft.Page, jogador, planeta, game_manager):
        self.page = page
        self.jogador = jogador
        self.planeta = planeta
        self.game_manager = game_manager
        self.content_ref = ft.Ref[ft.Container]()

        self.routes = [
            OverviewPage,
            NotificationsPage,
            MessagesPage,
            AnnouncementsPage,
            ResourcesPage,
            BuildingsPage,
            ResearchLabPage,
            HangarPage,
            SDPPage,
            CommandCorePage,
            FleetsPage,
            ObservatoryPage,
            TrafficPage,
            ExpeditionsPage,
            AdvancedBuildingsPage,
            #GatesPage,
            #EMEPage,
            #StarCannonPage,
            MoonsPage,
            ArchivesPage,
            BattleLogsPage,
            SimulatorsPage,
            RankingsPage,
            AlliancesPage,
            CommunityPage,
            MarketPage,
            CosmicEventsPage,
            StorePage,
        ]

    def navigate_to(self, index: int):
        page_class = self.routes[index]
        new_page = page_class(
            self.page,
            self.navigate_to,
            self.game_manager,
            self.planeta            
        ).build()
        self.content_ref.current.content = new_page
        self.page.update()
