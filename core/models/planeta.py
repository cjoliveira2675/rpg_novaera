from core.models.recursos import Recursos

class Planeta:
    def __init__(self, nome: str, construcoes: list = None):
        self.nome = nome
        self.recursos = Recursos()
        self.construcoes = construcoes if construcoes else []