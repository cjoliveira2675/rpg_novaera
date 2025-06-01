# RPG Nova Era - Model - Recursos
from .constructions import Construção, ConstruçãoTipo

class MinaMetal(Construção):
    def __init__(self, nivel=1, construido=True):
        super().__init__("Mina de Metal", ConstruçãoTipo.RECURSOS, nivel, construido)

    def custo_nivel(self, nivel) -> dict:
        return {
            "metal": 500 * nivel,
            "cristal": 300 * nivel,
            "prometium": 0
        }
    
    def produzir(self) -> dict:
        if not self.construido:
            return {}
        base = 200
        return {"metal": base * self.nivel}

    def consumir(self) -> dict:
        return {"energia": 20 * self.nivel}

    def requisitos(self) -> dict:
        return {}

class MinaCristal(Construção):
    def __init__(self, nivel=1, construido=True):
        super().__init__("Mina de Cristal", ConstruçãoTipo.RECURSOS, nivel, construido)

    def custo_nivel(self, nivel) -> dict:
        return {
            "metal": 500 * nivel,
            "cristal": 300 * nivel,
            "prometium": 0
        }
    
    def produzir(self) -> dict:
        if not self.construido:
            return {}
        base = 40
        return {"cristal": base * self.nivel}

    def consumir(self) -> dict:
        if self.construido:
            return {"energia": 4 * self.nivel}
        return {}

    def requisitos(self) -> dict:
        return {}

class SintetizadorPrometium(Construção):
    def __init__(self, nivel=1, construido=True):
        super().__init__("Sintetizador de Prometium", ConstruçãoTipo.RECURSOS, nivel, construido)

    def custo_nivel(self, nivel) -> dict:
        return {
            "metal": 500 * nivel,
            "cristal": 300 * nivel,
            "prometium": 0
        }
    
    def produzir(self) -> dict:
        if not self.construido:
            return {}
        base = 10
        return {"prometium": base * self.nivel}

    def consumir(self) -> dict:
        if self.construido:
            return {"energia": 8 * self.nivel}
        return {}

    def requisitos(self) -> dict:
        return {"metal": 200 * (self.nivel + 1), "cristal": 100 * (self.nivel + 1)}

class PlantaSolar(Construção):
    def __init__(self, nivel=1, construido=True):
        super().__init__("Planta Solar", ConstruçãoTipo.RECURSOS, nivel, construido)

    def custo_nivel(self, nivel) -> dict:
        return {
            "metal": 500 * nivel,
            "cristal": 300 * nivel,
            "prometium": 0
        }
    
    def produzir(self) -> dict:
        if not self.construido:
            return {}
        base = 100
        return {"energia": base * self.nivel}

    def consumir(self) -> dict:
        return {}

    def requisitos(self) -> dict:
        return {}

class Armazem(Construção):
    def __init__(self, nivel=1, construido=True, mineral=["Metal", "Cristal"]):
        super().__init__("Armazém", ConstruçãoTipo.RECURSOS, nivel, construido)
        self.capacidade = 5000 * self.nivel
        self.mineral = mineral

    def custo_nivel(self, nivel) -> dict:
        return {
            "metal": 500 * nivel,
            "cristal": 300 * nivel,
            "prometium": 0
        }
    
    def produzir(self) -> dict:
        return {}

    def consumir(self) -> dict:
        return {}

    def requisitos(self) -> dict:
        return {}

class TanquePrometium(Construção):
    def __init__(self, nivel=0, construido=False):
        super().__init__("Tanque de Prometium", ConstruçãoTipo.RECURSOS, nivel, construido)
        self.capacidade = 500 * self.nivel

    def custo_nivel(self, nivel) -> dict:
        return {
            "metal": 500 * nivel,
            "cristal": 300 * nivel,
            "prometium": 0
        }
    
    def produzir(self) -> dict:
        return {}

    def consumir(self) -> dict:
        return {}

    def requisitos(self) -> dict:
        return {"metal": 400 * self.nivel, "cristal": 100 * self.nivel}


class PlantaFusao(Construção):
    def __init__(self, nivel=0, construido=False):
        super().__init__("Planta de Fusão", ConstruçãoTipo.RECURSOS, nivel, construido)

    def custo_nivel(self, nivel) -> dict:
        return {
            "metal": 500 * nivel,
            "cristal": 300 * nivel,
            "prometium": 0
        }
    
    def produzir(self) -> dict:
        if self.construido:
            return {"energia": 300 * self.nivel}
        return {}

    def consumir(self) -> dict:
        if self.construido:
            return {"prometium": 10 * self.nivel}
        return {}

    def requisitos(self) -> dict:
        return {"metal": 1000 * (self.nivel + 1), "cristal": 500 * (self.nivel + 1), "prometium": 100 * (self.nivel + 1)}

class MineracaoEspacial(Construção):
    def __init__(self, nivel=0, construido=False):
        super().__init__("Unidade de Mineração Espacial", ConstruçãoTipo.ESTRUTURA_ESPACIAL, nivel, construido)
        self.capacidade_armazenamento = 1000 * self.nivel

    def custo_nivel(self, nivel) -> dict:
        return {
            "metal": 500 * nivel,
            "cristal": 300 * nivel,
            "prometium": 0
        }
    
    def produzir(self) -> dict:
        if self.construido:
            return {"metal": 50 * self.nivel, "cristal": 30 * self.nivel}
        return {}

    def consumir(self) -> dict:
        if self.construido:
            return {"energia": 15 * self.nivel}
        return {}

    def requisitos(self) -> dict:
        return {"metal": 800 * (self.nivel + 1), "cristal": 300 * (self.nivel + 1)}
    
class Hangar(Construção):
    def __init__(self, nivel=0, construido=False):
        super().__init__("Hangar", ConstruçãoTipo.SUPORTE_INFRA, nivel, construido)

    def custo_nivel(self, nivel) -> dict:
        return {
            "metal": 500 * nivel,
            "cristal": 300 * nivel,
            "prometium": 0
        }
    
    def produzir(self) -> dict:
        return {}

    def consumir(self) -> dict:
        return {"energia": 20 * self.nivel} if self.construido else {}

    def requisitos(self) -> dict:
        return {"metal": 500 * (self.nivel + 1)}

class LabPesquisas(Construção):
    def __init__(self, nivel=0, construido=False):
        super().__init__("Laboratório de Pesquisas", ConstruçãoTipo.SUPORTE_INFRA, nivel, construido)

    def custo_nivel(self, nivel) -> dict:
        return {
            "metal": 500 * nivel,
            "cristal": 300 * nivel,
            "prometium": 0
        }
    
    def produzir(self) -> dict:
        return {}

    def consumir(self) -> dict:
        return {"energia": 30 * self.nivel} if self.construido else {}

    def requisitos(self) -> dict:
        return {"metal": 700 * (self.nivel + 1), "cristal": 300 * (self.nivel + 1)}

class IndustriaRobotica(Construção):
    def __init__(self, nivel=0, construido=False):
        super().__init__("Indústria Robótica", ConstruçãoTipo.SUPORTE_INFRA, nivel, construido)

    def custo_nivel(self, nivel) -> dict:
        return {
            "metal": 500 * nivel,
            "cristal": 300 * nivel,
            "prometium": 0
        }
    
    def produzir(self) -> dict:
        return {"metal": 100 * self.nivel} if self.construido else {}

    def consumir(self) -> dict:
        return {"energia": 40 * self.nivel}

    def requisitos(self) -> dict:
        return {"metal": 900 * (self.nivel + 1), "cristal": 400 * (self.nivel + 1)}

class Refinaria(Construção):
    def __init__(self, nivel=0, construido=False):
        super().__init__("Refinaria", ConstruçãoTipo.SUPORTE_INFRA, nivel, construido)

    def custo_nivel(self, nivel) -> dict:
        return {
            "metal": 500 * nivel,
            "cristal": 300 * nivel,
            "prometium": 0
        }
    
    def produzir(self) -> dict:
        return {"prometium": 20 * self.nivel} if self.construido else {}

    def consumir(self) -> dict:
        return {"energia": 50 * self.nivel}

    def requisitos(self) -> dict:
        return {"metal": 1000 * (self.nivel + 1), "cristal": 500 * (self.nivel + 1)}

class Estaleiro(Construção):
    def __init__(self, nivel=0, construido=False):
        super().__init__("Estaleiro", ConstruçãoTipo.ESTRUTURA_ESPACIAL, nivel, construido)

    def custo_nivel(self, nivel) -> dict:
        return {
            "metal": 500 * nivel,
            "cristal": 300 * nivel,
            "prometium": 0
        }
    
    def produzir(self) -> dict:
        return {"naves": 5 * self.nivel} if self.construido else {}

    def consumir(self) -> dict:
        return {"energia": 60 * self.nivel}

    def requisitos(self) -> dict:
        return {"metal": 1500 * (self.nivel + 1), "cristal": 700 * (self.nivel + 1)}

class SiloMisseis(Construção):
    def __init__(self, nivel=0, construido=False):
        super().__init__("Silo de Mísseis", ConstruçãoTipo.SUPORTE_INFRA, nivel, construido)

    def custo_nivel(self, nivel) -> dict:
        return {
            "metal": 500 * nivel,
            "cristal": 300 * nivel,
            "prometium": 0
        }
    
    def produzir(self) -> dict:
        return {"misseis": 2 * self.nivel} if self.construido else {}

    def consumir(self) -> dict:
        return {"energia": 30 * self.nivel}

    def requisitos(self) -> dict:
        return {"metal": 1200 * (self.nivel + 1), "cristal": 500 * (self.nivel + 1)}

class SDP(Construção):
    def __init__(self, nivel=0, construido=False):
        super().__init__("Sistema de Defesa Planetária", ConstruçãoTipo.SUPORTE_INFRA, nivel, construido)

    def custo_nivel(self, nivel) -> dict:
        return {
            "metal": 500 * nivel,
            "cristal": 300 * nivel,
            "prometium": 0
        }
    
    def produzir(self) -> dict:
        return {}

    def consumir(self) -> dict:
        return {"energia": 100 * self.nivel}

    def requisitos(self) -> dict:
        return {"metal": 2000 * (self.nivel + 1), "cristal": 1000 * (self.nivel + 1)}

class BaseLunar(Construção):
    def __init__(self, nivel=0, construido=False):
        super().__init__("Base Lunar", ConstruçãoTipo.ESTRUTURA_ESPACIAL, nivel, construido)

    def custo_nivel(self, nivel) -> dict:
        return {
            "metal": 500 * nivel,
            "cristal": 300 * nivel,
            "prometium": 0
        }
    
    def produzir(self) -> dict:
        return {"metal": 40 * self.nivel, "cristal": 20 * self.nivel} if self.construido else {}

    def consumir(self) -> dict:
        return {"energia": 70 * self.nivel}

    def requisitos(self) -> dict:
        return {"metal": 2500 * (self.nivel + 1), "cristal": 1200 * (self.nivel + 1)}
    
class NucleoComando(Construção):
    def __init__(self, nivel=0, construido=False):
        super().__init__("Núcleo de Comandos", ConstruçãoTipo.SUPORTE_INFRA, nivel, construido)

    def custo_nivel(self, nivel) -> dict:
        return {
            "metal": 500 * nivel,
            "cristal": 300 * nivel,
            "prometium": 0
        }
    
    def produzir(self) -> dict:
        return {"metal": 40 * self.nivel, "cristal": 20 * self.nivel} if self.construido else {}

    def consumir(self) -> dict:
        return {"energia": 70 * self.nivel}

    def requisitos(self) -> dict:
        return {"metal": 2500 * (self.nivel + 1), "cristal": 1200 * (self.nivel + 1)}
    
class Observatorio(Construção):
    def __init__(self, nivel=0, construido=False):
        super().__init__("Observatório", ConstruçãoTipo.SUPORTE_INFRA, nivel, construido)

    def custo_nivel(self, nivel) -> dict:
        return {
            "metal": 500 * nivel,
            "cristal": 300 * nivel,
            "prometium": 0
        }
    
    def produzir(self) -> dict:
        return {"metal": 40 * self.nivel, "cristal": 20 * self.nivel} if self.construido else {}

    def consumir(self) -> dict:
        return {"energia": 70 * self.nivel}

    def requisitos(self) -> dict:
        return {"metal": 2500 * (self.nivel + 1), "cristal": 1200 * (self.nivel + 1)}
    
class ControleAvancado(Construção):
    def __init__(self, nivel=0, construido=False):
        super().__init__("Controle de estruturas avançadas", ConstruçãoTipo.SUPORTE_INFRA, nivel, construido)

    def custo_nivel(self, nivel) -> dict:
        return {
            "metal": 500 * nivel,
            "cristal": 300 * nivel,
            "prometium": 0
        }
    
    def produzir(self) -> dict:
        return {"metal": 40 * self.nivel, "cristal": 20 * self.nivel} if self.construido else {}

    def consumir(self) -> dict:
        return {"energia": 70 * self.nivel}

    def requisitos(self) -> dict:
        return {"metal": 2500 * (self.nivel + 1), "cristal": 1200 * (self.nivel + 1)}