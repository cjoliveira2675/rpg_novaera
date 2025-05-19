import flet as ft

class HomePage:
    def __init__(self, page: ft.Page):
        self.page = page

    def build(self):
        self.page.add(ft.Text("Bem-vindo ao RPG Nova Era!"))
