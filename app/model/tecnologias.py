from abc import ABC, abstractmethod
from enum import Enum

class TecnologiaTipo(Enum):
    ENERGIA = "Energia"
    MINERACAO = "Mineração"
    INFORMACAO = "Informação"
    ESPACIAL = "Espacial"
    UNIDADES = "Unidades"

class Tecnologia(ABC):
    def __init__(self, nome: str, descricao: str, tipo: TecnologiaTipo, consumo: dict, tempo_pesquisa: int, max_lvl: int):
        self.nome = nome
        self.descricao = descricao
        self.tipo = tipo
        self.consumo = consumo
        self.tempo_pesquisa = tempo_pesquisa
        self.pesquisado = False
        self.max_lvl = max_lvl

    def pesquisar(self, recursos: dict) -> bool:
        if self.pesquisado:
            print(f"{self.nome} já foi pesquisada.")
            return False

        if all(recursos[res] >= qty for res, qty in self.consumo.items()):
            for res, qty in self.consumo.items():
                recursos[res] -= qty
            self.pesquisado = True
            print(f"{self.nome} foi pesquisada com sucesso.")
            return True

        print(f"Recursos insuficientes para pesquisar {self.nome}")
        return False

    @abstractmethod
    def requisitos(self) -> dict:
        pass
