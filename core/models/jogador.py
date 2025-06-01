# core/models/jogador.py
class Jogador:
    def __init__(self, nome: str = "Armagtera", tecnologias: list = None):
        self.nome = nome
        self.tecnologias = tecnologias if tecnologias else []