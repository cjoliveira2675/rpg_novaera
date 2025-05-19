from abc import ABC, abstractmethod
from enum import Enum

class TecnologiaTipo(Enum):
    ENERGIA = "Energia"
    MINERACAO = "Mineração"
    INFORMACAO = "Informação"
    ESPACIAL = "Espacial"
    UNIDADES = "Unidades"

class Tecnologia(ABC):
    """
    Classe base para tecnologias do jogo.
    """
    def __init__(self, nome: str, descricao: str, tipo: TecnologiaTipo, consumo: dict, tempo_pesquisa: int, pesquisada: bool, max_lvl: int):
        self.nome = nome
        self.descricao = descricao
        self.tipo = tipo
        self.consumo = consumo
        self.tempo_pesquisa = tempo_pesquisa
        self.pesquisada = pesquisada
        self.max_lvl = max_lvl

    def pesquisar(self, recursos: dict) -> bool:
        if self.pesquisada:
            print(f"{self.nome} já foi pesquisada.")
            return False

        if all(recursos[res] >= qty for res, qty in self.consumo.items()):
            for res, qty in self.consumo.items():
                recursos[res] -= qty
            self.pesquisada = True
            print(f"{self.nome} foi pesquisada com sucesso.")
            return True

        print(f"Recursos insuficientes para pesquisar {self.nome}")
        return False

    @abstractmethod
    def requisitos(self) -> dict:
        pass
