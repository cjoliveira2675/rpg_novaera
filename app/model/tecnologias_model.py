from tecnologias import Tecnologia, TecnologiaTipo

class MineraçãoAvancada(Tecnologia):
    def __init__(self):
        super().__init__(
            nome="Mineração Avançada",
            descricao="Permite maior volume de extração de recursos.",
            tipo=TecnologiaTipo.MINERACAO,
            consumo={"Metal": 200, "Cristal": 150},
            tempo_pesquisa=3,
            max_lvl=1
        )   

    def requisitos(self) -> dict:
        return {"Mineração avançada": "a"}

class RecursosProfundidade(Tecnologia):
    def __init__(self):
        super().__init__(
            nome="Recursos em Profundidade",
            descricao="Permite extração de recursos em larga escala.",
            tipo=TecnologiaTipo.MINERACAO,
            consumo={"Metal": 300, "Cristal": 250, "Prometium": 150},
            tempo_pesquisa=7,
            max_lvl=1
        )

    def requisitos(self) -> dict:
        return {"Recursos em Profundidade": "a"}

class EspecializacaoMineracao(Tecnologia):
    def __init__(self):
        super().__init__(
            nome="Especialização em Mineração",
            descricao="Mineração mais eficiente.",
            tipo=TecnologiaTipo.MINERACAO,
            consumo={"Metal": 500, "Cristal": 400},
            tempo_pesquisa=10,
            max_lvl=1
        )

    def requisitos(self) -> dict:
        return {"Especialização em Mineração": "a"}

class ProducaoEnergiaAvancada(Tecnologia):
    def __init__(self):
        super().__init__(
            nome="Produção de Energia Avançada",
            descricao="",
            tipo=TecnologiaTipo.ENERGIA,
            consumo={"Metal": 300, "Cristal": 200},
            tempo_pesquisa=6,
            max_lvl=5
        )

    def requisitos(self) -> dict:
        return {"Produção de Energia Avançada": ""}

class TecnologiaFusao(Tecnologia):
    def __init__(self):
        super().__init__(
            nome="Tecnologia de Fusão",
            descricao="",
            tipo=TecnologiaTipo.ENERGIA,
            consumo={"Metal": 500, "Cristal": 400, "Prometium": 250},
            tempo_pesquisa=8,
            max_lvl=1
        )

    def requisitos(self) -> dict:
        return {"Tecnologia de Fusão": ""}

class FontesSubatomicas(Tecnologia):
    def __init__(self):
        super().__init__(
            nome="Fontes Subatomicas",
            descricao="",
            tipo=TecnologiaTipo.ENERGIA,
            consumo={"Metal": 700, "Cristal": 600},
            tempo_pesquisa=12,
            max_lvl=1
        )

    def requisitos(self) -> dict:
        return {"Fontes Subatomicas": ""}

class FontesExternas(Tecnologia):
    def __init__(self):
        super().__init__(
            nome="Gravitação", 
            descricao="",
            tipo=TecnologiaTipo.ENERGIA,
            consumo={"Metal": 700, "Cristal": 600},
            tempo_pesquisa=8,
            max_lvl=1
        )

    def requisitos(self) -> dict:
        return {"Gravitação": ""}
    
class Optica(Tecnologia):
    def __init__(self):
        super().__init__(
            nome="Refração avançada",
            descricao="",
            tipo=TecnologiaTipo.INFORMACAO,
            consumo={"Metal": 700, "Cristal": 500},
            tempo_pesquisa=10,
            max_lvl=10
        )

    def requisitos(self):
        return {"Refração avançada": ""}

class FaixasFrequencia(Tecnologia):
    def __init__(self):
        super().__init__(
            nome="Estudo de ondas eletromagnéticas",
            descricao="",
            tipo=TecnologiaTipo.INFORMACAO,
            consumo={},
            tempo_pesquisa=10,
            max_lvl=1
        )

    def requisitos(self):
        return {}
    
class RedeComputadores(Tecnologia):
    def __init__(self):
        super().__init__(
            nome="Rede de computadores",
            descricao="",
            tipo=TecnologiaTipo.INFORMACAO,
            consumo={},
            tempo_pesquisa=10,
            max_lvl=4
        )

    def requisitos(self):
        return {}
    
class IA(Tecnologia):
    def __init__(self):
        super().__init__(
            nome="Robótica avançada",
            descricao="",
            tipo=TecnologiaTipo.INFORMACAO,
            consumo={},
            tempo_pesquisa=10,
            max_lvl=1
        )

    def requisitos(self):
        return {}
    
class Astrofisica(Tecnologia):
    def __init__(self):
        super().__init__(
            nome="Expedições interestelares",
            descricao="",
            tipo=TecnologiaTipo.INFORMACAO,
            consumo={},
            tempo_pesquisa=10,
            max_lvl=10
        )

    def requisitos(self):
        return {}

class Interferencia(Tecnologia):
    def __init__(self):
        super().__init__(
            nome="Estudo avançado de fases",
            descricao="",
            tipo=TecnologiaTipo.INFORMACAO,
            consumo={},
            tempo_pesquisa=10,
            max_lvl=1
        )

    def requisitos(self):
        return {}
    
class FasesCombinadas(Tecnologia):
    def __init__(self):
        super().__init__(
            nome="Assimilação de Frequência",
            descricao="",
            tipo=TecnologiaTipo.INFORMACAO,
            consumo={},
            tempo_pesquisa=10,
            max_lvl=4
        )

    def requisitos(self):
        return {}
    
class VirusMilitar(Tecnologia):
    def __init__(self):
        super().__init__(
            nome="Análise específica",
            descricao="",
            tipo=TecnologiaTipo.INFORMACAO,
            consumo={},
            tempo_pesquisa=10,
            max_lvl=1
        )

    def requisitos(self):
        return {}
    
class MotorCombustao(Tecnologia):
    def __init__(self):
        super().__init__(
            nome="Motor de Combustão",
            descricao="",
            tipo=TecnologiaTipo.ESPACIAL,
            consumo={},
            tempo_pesquisa=10,
            max_lvl=1
        )
    
    def requisitos(self):
        return {}
    
class MotorImpulsão(Tecnologia):
    def __init__(self):
        super().__init__(
            nome="Motor de impulsão",
            descricao="",
            tipo=TecnologiaTipo.ESPACIAL,
            consumo={},
            tempo_pesquisa=10,
            max_lvl=1
        )
    
    def requisitos(self):
        return {}

class MotorHiperespaço(Tecnologia):
    def __init__(self):
        super().__init__(
            nome="Motor propulsor de hiperespaço",
            descricao="",
            tipo=TecnologiaTipo.ESPACIAL,
            consumo={},
            tempo_pesquisa=10,
            max_lvl=1
        )
    
    def requisitos(self):
        return {}
    
class MotorDobra(Tecnologia):
    def __init__(self):
        super().__init__(
            nome="Motor de Dobra espacial",
            descricao="",
            tipo=TecnologiaTipo.ESPACIAL,
            consumo={},
            tempo_pesquisa=10,
            max_lvl=1
        )
    
    def requisitos(self):
        return {}
    
class FendaDimensional(Tecnologia):
    def __init__(self):
        super().__init__(
            nome="Fenda dimensional",
            descricao="",
            tipo=TecnologiaTipo.ESPACIAL,
            consumo={},
            tempo_pesquisa=10,
            max_lvl=1
        )
    
    def requisitos(self):
        return {}

class ReatorQuantico(Tecnologia):
    def __init__(self):
        super().__init__(
            nome="Reator de salto quântico",
            descricao="",
            tipo=TecnologiaTipo.ESPACIAL,
            consumo={},
            tempo_pesquisa=10,
            max_lvl=1
        )
    
    def requisitos(self):
        return {}
    
class Fundição(Tecnologia):
    def __init__(self):
        super().__init__(
            nome="Fundição",
            descricao="",
            tipo=TecnologiaTipo.UNIDADES,
            consumo={},
            tempo_pesquisa=10,
            max_lvl=1
        )
    
    def requisitos(self):
        return {}
    
class EstruturasMelhoradas (Tecnologia):
    def __init__(self):
        super().__init__(
            nome="Estruturas Melhoradas",
            descricao="",
            tipo=TecnologiaTipo.UNIDADES,
            consumo={},
            tempo_pesquisa=10,
            max_lvl=6
        )
    
    def requisitos(self):
        return {} 

class DisparosRápidos(Tecnologia):
    def __init__(self):
        super().__init__(
            nome="Disparos rápidos",
            descricao="",
            tipo=TecnologiaTipo.UNIDADES,
            consumo={},
            tempo_pesquisa=10,
            max_lvl=6
        )
    
    def requisitos(self):
        return {}

class FuselagemMelhorada(Tecnologia):
    def __init__(self):
        super().__init__(
            nome="Fuselagem melhorada",
            descricao="",
            tipo=TecnologiaTipo.UNIDADES,
            consumo={},
            tempo_pesquisa=10,
            max_lvl=1
        )
    
    def requisitos(self):
        return {}

class ArmasPesadas(Tecnologia):
    def __init__(self):
        super().__init__(
            nome="Armas pesadas",
            descricao="",
            tipo=TecnologiaTipo.UNIDADES,
            consumo={},
            tempo_pesquisa=10,
            max_lvl=1
        )
    
    def requisitos(self):
        return {}

