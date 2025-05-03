import flet as ft

class SideMenu(ft.Container):
    def __init__(self, page: ft.Page, on_navigate):
        super().__init__(
            width=220,
            bgcolor=ft.colors.BLUE_GREY_700,
            padding=15,
            expand=True,
            content=ft.Column(
                scroll=ft.ScrollMode.AUTO,
                spacing=6,
                controls=[
                    self.menu_button("Visão Geral", 0, on_navigate),
                    ft.Divider(color=ft.colors.WHITE),
                    self.menu_button("Notificações", 1, on_navigate),
                    self.menu_button("Mensagens", 2, on_navigate),
                    self.menu_button("Comunicados", 3, on_navigate),
                    ft.Divider(color=ft.colors.WHITE),
                    self.menu_button("Recursos", 4, on_navigate),
                    self.menu_button("Laboratório", 5, on_navigate),
                    self.menu_button("Construções", 6, on_navigate),
                    self.menu_button("Hangar", 7, on_navigate),
                    self.menu_button("Sistema de Defesa", 8, on_navigate),
                    ft.Divider(color=ft.colors.WHITE),
                    self.menu_button("Núcleo de Comandos", 9, on_navigate),
                    self.menu_button("Frotas", 10, on_navigate),
                    self.menu_button("Observatório", 11, on_navigate),
                    self.menu_button("Tráfego", 12, on_navigate),
                    ft.Divider(color=ft.colors.WHITE),
                    self.menu_button("Arquivos", 13, on_navigate),
                    self.menu_button("Log de Combates", 14, on_navigate),
                    self.menu_button("Simuladores", 15, on_navigate),
                    self.menu_button("Rankings", 16, on_navigate),
                    ft.Divider(color=ft.colors.WHITE),
                    self.menu_button("Estruturas Avançadas", 17, on_navigate),
                    self.menu_button("Portal", 18, on_navigate),
                    self.menu_button("E.M.E", 19, on_navigate),
                    self.menu_button("Canhão de Neutrons", 20, on_navigate),
                    self.menu_button("Luas", 21, on_navigate),
                    ft.Divider(color=ft.colors.WHITE),
                    self.menu_button("Comunidade", 22, on_navigate),
                    self.menu_button("Mercado", 23, on_navigate),
                    self.menu_button("Aliança", 24, on_navigate),
                    self.menu_button("Loja", 25, on_navigate),
                    ft.Divider(color=ft.colors.WHITE),
                    self.menu_button("Eventos Cósmicos", 26, on_navigate),
                    self.menu_button("Expedições", 27, on_navigate),
                ]
            )
        )
        

    def menu_button(self, label, index, on_click):
        return ft.ElevatedButton(
            text=label,
            on_click=lambda _: on_click(index),
            height=26,
            width=200,
            bgcolor=ft.colors.BLUE_GREY_900,
            color=ft.colors.WHITE,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=6),
                padding=ft.Padding(6, 4, 4, 0),
                text_style=ft.TextStyle(
                    size=12,
                    weight=ft.FontWeight.W_600,
                    font_family="Courier New"
                ),
                overlay_color=ft.colors.BLUE_GREY_200,  # toque visual ao clicar
            )
        )
