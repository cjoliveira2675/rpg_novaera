# RPG Nova Era - Service - Recursos
from app.model.constructions_model import MinaMetal, MinaCristal, SintetizadorPrometium, PlantaSolar, Meteoro

class Planeta:
    def __init__(self):
        self.recursos = {
            'metal': 2500,
            'cristal': 1000,
            'prometium': 0,
            'energia': 100
        }
        self.construcoes = [MinaMetal(), PlantaSolar()]
        self.meteoros = []

    def atualizar_recursos(self):
        for construcao in self.construcoes:
            self.recursos['metal'] += construcao.producao if isinstance(construcao, MinaMetal) else 0
            self.recursos['cristal'] += construcao.producao if isinstance(construcao, MinaCristal) else 0
            self.recursos['prometium'] += construcao.producao if isinstance(construcao, SintetizadorPrometium) else 0
            self.recursos['energia'] += construcao.producao if isinstance(construcao, PlantaSolar) else 0
            self.recursos['energia'] -= construcao.consumo

        # Verifica meteoros e aplica extração
        for meteoro in self.meteoros:
            if meteoro.tipo == 'Fogo':
                self.recursos['metal'] += meteoro.extrair(20)
            elif meteoro.tipo == 'Cristal':
                self.recursos['cristal'] += meteoro.extrair(15)
            elif meteoro.tipo == 'Gelo':
                self.recursos['prometium'] += meteoro.extrair(10)
            elif meteoro.tipo == 'Estelar':
                self.recursos['metal'] += meteoro.extrair(30)
                self.recursos['cristal'] += meteoro.extrair(20)

        # Garantir que os recursos não excedam a capacidade
        self.recursos['metal'] = min(self.recursos['metal'], 5000)
        self.recursos['cristal'] = min(self.recursos['cristal'], 2000)
        self.recursos['prometium'] = min(self.recursos['prometium'], 500)
        self.recursos['energia'] = min(self.recursos['energia'], 200)

        print(f"Recursos Atualizados: {self.recursos}")