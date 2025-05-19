from core.controllers.game_manager import GameManager
from core.models.tecnologias_model import MineracaoAvancada
from core.models.constructions_model import MinaMetal, PlantaSolar
from core.models.recursos import Recursos
import time

# Simulação de jogador e planeta
class Jogador:
    def __init__(self):
        self.tecnologias = [MineracaoAvancada(pesquisada=True)]

class Planeta:
    def __init__(self):
        self.nome = "Éden Prime"
        self.recursos = Recursos(metal=2500, cristal=1000, prometium=0, energia=100)
        self.construcoes = [
            MinaMetal(nivel=1, construido=True),
            PlantaSolar(nivel=1, construido=True)
        ]

# Inicializa sistema
jogador = Jogador()
planeta = Planeta()
gerenciador = GameManager(jogador, planeta)

# Roda 5 ticks com intervalo
for tick in range(5):
    print(f"⏱️ Tick {tick + 1}")
    gerenciador.processar_tick()
    time.sleep(1)