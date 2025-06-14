# RPG Nova Era - Model - Construções
from abc import ABC, abstractmethod
from enum import Enum

class ConstruçãoTipo(Enum):
    RECURSOS = ("mina", "armazem", "planta")
    SUPORTE_INFRA = ("suporte", "hangar", "robótica")
    ESTRUTURA_ESPACIAL = ("espacial", "estaleiro", "base lunar")
    ESTRUTURA_AVANCADA = ("avançada", "portal", "eme", "canhão estelar")

class Construção(ABC):
    """
    Classe base para construçãos do jogo.
    """
    def __init__(self, nome: str, tipo: ConstruçãoTipo, nivel: int = 0, construido: bool = False):
        self.nome = nome
        self.tipo = tipo
        self.nivel = nivel
        self.construido = construido

    def construir(self, recursos: dict) -> bool:
        custo = self.custo_nivel(1)
        if all(recursos.get(res, 0) >= valor for res, valor in custo.items()):
            for res, valor in custo.items():
                recursos[res] -= valor
            self.construido = True
            self.nivel = 1
            print(f"{self.nome} foi construída e está no nível 1.")
            return True
        print(f"❌ Recursos insuficientes para construir {self.nome}. Custo: {custo}")
        return False

    def evoluir(self, recursos: dict) -> bool:
        custo = self.custo_nivel(self.nivel + 1)
        if all(recursos.get(res, 0) >= valor for res, valor in custo.items()):
            for res, valor in custo.items():
                recursos[res] = recursos.get(res, 0) - valor
            self.nivel += 1
            print(f"{self.nome} evoluiu para o nível {self.nivel}")
            return True
        print(f"Recursos insuficientes para evoluir {self.nome}. Custo: {custo}")
        return False

    def produzir(self) -> dict:
        """Método padrão para construções sem produção passiva."""
        return {}
    
    @abstractmethod
    def custo_nivel(self, nivel) -> dict:
        pass
    
    @abstractmethod
    def consumir(self) -> dict:
        pass

    @abstractmethod
    def requisitos(self) -> dict:
        pass
