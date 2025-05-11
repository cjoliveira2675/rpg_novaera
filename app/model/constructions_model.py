# RPG Nova Era - Model - Recursos
from model.constructions import Construção, ConstruçãoTipo

class MinaMetal(Construção):
    def __init__(self, nivel=1, construido=True):
        super().__init__("Mina de Metal", ConstruçãoTipo.MINA_METAL, nivel, construido)

    def produzir(self, energia_disponivel: int) -> dict:
        if self.construido and energia_disponivel >= (5 * self.nivel):
            return {"metal": 50 * self.nivel}
        return {}

    def consumir(self) -> dict:
        if self.construido:
            return {"energia": 5 * self.nivel}
        return {}

    def requisitos(self) -> dict:
        return {"metal": 100 * (self.nivel + 1)}

class MinaCristal(Construção):
    def __init__(self, nivel=1, construido=True):
        super().__init__("Mina de Cristal", ConstruçãoTipo.MINA_CRISTAL, nivel, construido)

    def produzir(self, energia_disponivel: int) -> dict:
        if self.construido and energia_disponivel >= (4 * self.nivel):
            return {"cristal": 30 * self.nivel}
        return {}

    def consumir(self) -> dict:
        if self.construido:
            return {"energia": 4 * self.nivel}
        return {}

    def requisitos(self) -> dict:
        return {"metal": 150 * (self.nivel + 1), "cristal": 50 * (self.nivel + 1)}

class SintetizadorPrometium(Construção):
    def __init__(self, nivel=1, construido=True):
        super().__init__("Sintetizador de Prometium", ConstruçãoTipo.SINTETIZADOR_PROMETIUM, nivel, construido)

    def produzir(self, energia_disponivel: int) -> dict:
        if self.construido and energia_disponivel >= (8 * self.nivel):
            return {"prometium": 10 * self.nivel}
        return {}

    def consumir(self) -> dict:
        if self.construido:
            return {"energia": 8 * self.nivel}
        return {}

    def requisitos(self) -> dict:
        return {"metal": 200 * (self.nivel + 1), "cristal": 100 * (self.nivel + 1)}

class PlantaSolar(Construção):
    def __init__(self, nivel=1, construido=True):
        super().__init__("Planta Solar", ConstruçãoTipo.PLANTA_SOLAR, nivel, construido)

    def produzir(self) -> dict:
        return {"energia": 100 * self.nivel}

    def consumir(self) -> dict:
        return {}

    def requisitos(self) -> dict:
        return {"metal": 100 * self.nivel}

class Armazem(Construção):
    def __init__(self, nivel=1, construido=True):
        super().__init__("Armazém", ConstruçãoTipo.ARMAZEM, nivel, construido)
        self.capacidade = 5000 * self.nivel

    def produzir(self) -> dict:
        return {}

    def consumir(self) -> dict:
        return {}

    def requisitos(self) -> dict:
        return {"metal": 300 * self.nivel}

class TanquePrometium(Construção):
    def __init__(self, nivel=0, construido=False):
        super().__init__("Tanque de Prometium", ConstruçãoTipo.TANQUE, nivel, construido)
        self.capacidade = 500 * self.nivel

    def produzir(self) -> dict:
        return {}

    def consumir(self) -> dict:
        return {}

    def requisitos(self) -> dict:
        return {"metal": 400 * self.nivel, "cristal": 100 * self.nivel}


class PlantaFusao(Construção):
    def __init__(self, nivel=0, construido=False):
        super().__init__("Planta de Fusão", ConstruçãoTipo.PLANTA_FUSAO, nivel, construido)

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
        super().__init__("Unidade de Mineração Espacial", ConstruçãoTipo.MINERACAO_ESPACIAL, nivel, construido)
        self.capacidade_armazenamento = 1000 * self.nivel

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
        super().__init__("Hangar", ConstruçãoTipo.HANGAR, nivel, construido)

    def produzir(self) -> dict:
        return {}

    def consumir(self) -> dict:
        return {"energia": 20 * self.nivel} if self.construido else {}

    def requisitos(self) -> dict:
        return {"metal": 500 * (self.nivel + 1)}

class LabPesquisas(Construção):
    def __init__(self, nivel=0, construido=False):
        super().__init__("Laboratório de Pesquisas", ConstruçãoTipo.LAB_PESQUISAS, nivel, construido)

    def produzir(self) -> dict:
        return {}

    def consumir(self) -> dict:
        return {"energia": 30 * self.nivel} if self.construido else {}

    def requisitos(self) -> dict:
        return {"metal": 700 * (self.nivel + 1), "cristal": 300 * (self.nivel + 1)}

class IndustriaRobotica(Construção):
    def __init__(self, nivel=0, construido=False):
        super().__init__("Indústria Robótica", ConstruçãoTipo.INDUSTRIA_ROBOTICA, nivel, construido)

    def produzir(self) -> dict:
        return {"metal": 100 * self.nivel} if self.construido else {}

    def consumir(self) -> dict:
        return {"energia": 40 * self.nivel}

    def requisitos(self) -> dict:
        return {"metal": 900 * (self.nivel + 1), "cristal": 400 * (self.nivel + 1)}

class Refinaria(Construção):
    def __init__(self, nivel=0, construido=False):
        super().__init__("Refinaria", ConstruçãoTipo.CONSTRUCAO_ESPACIAL, nivel, construido)

    def produzir(self) -> dict:
        return {"prometium": 20 * self.nivel} if self.construido else {}

    def consumir(self) -> dict:
        return {"energia": 50 * self.nivel}

    def requisitos(self) -> dict:
        return {"metal": 1000 * (self.nivel + 1), "cristal": 500 * (self.nivel + 1)}

class Estaleiro(Construção):
    def __init__(self, nivel=0, construido=False):
        super().__init__("Estaleiro", ConstruçãoTipo.CONSTRUCAO_ESPACIAL, nivel, construido)

    def produzir(self) -> dict:
        return {"naves": 5 * self.nivel} if self.construido else {}

    def consumir(self) -> dict:
        return {"energia": 60 * self.nivel}

    def requisitos(self) -> dict:
        return {"metal": 1500 * (self.nivel + 1), "cristal": 700 * (self.nivel + 1)}

class SiloMisseis(Construção):
    def __init__(self, nivel=0, construido=False):
        super().__init__("Silo de Mísseis", ConstruçãoTipo.SILO_MISSEIS, nivel, construido)

    def produzir(self) -> dict:
        return {"misseis": 2 * self.nivel} if self.construido else {}

    def consumir(self) -> dict:
        return {"energia": 30 * self.nivel}

    def requisitos(self) -> dict:
        return {"metal": 1200 * (self.nivel + 1), "cristal": 500 * (self.nivel + 1)}

class SDP(Construção):
    def __init__(self, nivel=0, construido=False):
        super().__init__("Sistema de Defesa Planetária", ConstruçãoTipo.CONSTRUCAO_ESPACIAL, nivel, construido)

    def produzir(self) -> dict:
        return {}

    def consumir(self) -> dict:
        return {"energia": 100 * self.nivel}

    def requisitos(self) -> dict:
        return {"metal": 2000 * (self.nivel + 1), "cristal": 1000 * (self.nivel + 1)}

class BaseLunar(Construção):
    def __init__(self, nivel=0, construido=False):
        super().__init__("Base Lunar", ConstruçãoTipo.CONSTRUCAO_ESPACIAL, nivel, construido)

    def produzir(self) -> dict:
        return {"metal": 40 * self.nivel, "cristal": 20 * self.nivel} if self.construido else {}

    def consumir(self) -> dict:
        return {"energia": 70 * self.nivel}

    def requisitos(self) -> dict:
        return {"metal": 2500 * (self.nivel + 1), "cristal": 1200 * (self.nivel + 1)}
    
class NucleoComando(Construção):
    def __init__(self, nivel=0, construido=False):
        super().__init__("Núcleo de Comandos", ConstruçãoTipo.CONSTRUCAO_ESPACIAL, nivel, construido)

    def produzir(self) -> dict:
        return {"metal": 40 * self.nivel, "cristal": 20 * self.nivel} if self.construido else {}

    def consumir(self) -> dict:
        return {"energia": 70 * self.nivel}

    def requisitos(self) -> dict:
        return {"metal": 2500 * (self.nivel + 1), "cristal": 1200 * (self.nivel + 1)}
    
class Observatorio(Construção):
    def __init__(self, nivel=0, construido=False):
        super().__init__("Observatório", ConstruçãoTipo.CONSTRUCAO_ESPACIAL, nivel, construido)

    def produzir(self) -> dict:
        return {"metal": 40 * self.nivel, "cristal": 20 * self.nivel} if self.construido else {}

    def consumir(self) -> dict:
        return {"energia": 70 * self.nivel}

    def requisitos(self) -> dict:
        return {"metal": 2500 * (self.nivel + 1), "cristal": 1200 * (self.nivel + 1)}
    
class ControleAvancado(Construção):
    def __init__(self, nivel=0, construido=False):
        super().__init__("Controle de estruturas avançadas", ConstruçãoTipo.CONSTRUCAO_ESPACIAL, nivel, construido)

    def produzir(self) -> dict:
        return {"metal": 40 * self.nivel, "cristal": 20 * self.nivel} if self.construido else {}

    def consumir(self) -> dict:
        return {"energia": 70 * self.nivel}

    def requisitos(self) -> dict:
        return {"metal": 2500 * (self.nivel + 1), "cristal": 1200 * (self.nivel + 1)}