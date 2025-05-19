# RPG Nova Era - Model - Meteoro
from enum import Enum

class MeteoroTipo(Enum):
    FOGO = "Fogo"
    CRISTAL = "Cristal"
    GELO = "Gelo"
    ESTELAR = "Estelar"

class Meteoro:
    def __init__(self, tipo: MeteoroTipo, quantidade: int):
        self.tipo = tipo
        self.quantidade = quantidade

    def extrair(self, quantidade: int) -> int:
        extraido = min(self.quantidade, quantidade)
        self.quantidade -= extraido
        return extraido