from core.models.recursos import Recursos
from core.models.constructions_model import *

class Planeta:
    def __init__(self, nome: str = "Fiatera"):
        self.nome = nome
        self.recursos = Recursos()
        
        # Todas as construções padrão
        self.mina_metal = MinaMetal(nivel=0, construido=False)
        self.mina_cristal = MinaCristal(nivel=0, construido=False)
        self.planta_solar = PlantaSolar(nivel=0, construido=False)
        self.armazem_metal = Armazem(nivel=0, construido=False, mineral="Metal")
        self.armazem_cristal = Armazem(nivel=0, construido=False, mineral="Cristal")

        # Lista para iteração nos ticks
        self.construcoes = [
            self.mina_metal,
            self.mina_cristal,
            self.planta_solar,
            self.armazem_metal,
            self.armazem_cristal
        ]