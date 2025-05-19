from core.models.recursos import Recursos
from core.models.tecnologias_model import *
from core.models.constructions_model import *

class GameManager:
    def __init__(self, jogador, planeta):
        self.jogador = jogador
        self.planeta = planeta
        self.recursos = planeta.recursos
        self.construcoes = planeta.construcoes
        self.tecnologias = jogador.tecnologias
        self.fila_construcoes = []
        self.fila_pesquisas = []

    def atualizar_recursos(self):
        """
        Produz recursos com base nos níveis das minas e nas tecnologias pesquisadas.
        Considera consumo e produção de energia.
        """
        producao = {"metal": 0, "cristal": 0, "prometium": 0}
        energia_disponivel = 0
        energia_necessaria = 0

        for construcao in self.construcoes:
            if not construcao.construido:
                continue

            prod = construcao.produzir()
            cons = construcao.consumir()

            for recurso, valor in prod.items():
                if recurso in producao:
                    producao[recurso] += valor
                elif recurso == "energia":
                    energia_disponivel += valor

            energia_necessaria += cons.get("energia", 0)

        # Aplicar bônus por tecnologias
        for tecnologia in self.tecnologias:
            if not tecnologia.pesquisada:
                continue

            if isinstance(tecnologia, MineracaoAvancada):
                producao["metal"] += 1500
                producao["cristal"] += 800
                producao["prometium"] += 500

            elif isinstance(tecnologia, RecursosProfundidade):
                producao["metal"] += 10000
                producao["cristal"] += 6000
                producao["prometium"] += 3750
                energia_necessaria += 60

            elif isinstance(tecnologia, EspecializacaoMineracao):
                for k in producao:
                    producao[k] *= 1.15
                energia_necessaria *= 1.10

        # Aplicar produção se energia suficiente
        if energia_disponivel >= energia_necessaria:
            self.recursos.metal += int(producao["metal"])
            self.recursos.cristal += int(producao["cristal"])
            self.recursos.prometium += int(producao["prometium"])
            print(f"✅ Recursos atualizados: {producao}")
        else:
            print(f"⚠️ Energia insuficiente. Disponível: {energia_disponivel}, Necessária: {energia_necessaria}")


    def processar_fila_construcoes(self):
        """
        Processa a próxima ordem de construção da fila, se houver recursos disponíveis.
        """
        if not self.fila_construcoes:
            return

        construcao = self.fila_construcoes[0]

        # Verifica se a construção já foi construída ou é evolução
        if construcao.construido:
            custo = construcao.custo_nivel(construcao.nivel + 1)
        else:
            custo = construcao.custo_nivel(1)

        if (self.recursos.metal >= custo.get("metal", 0) and
            self.recursos.cristal >= custo.get("cristal", 0) and
            self.recursos.prometium >= custo.get("prometium", 0)):

            # Desconta recursos
            self.recursos.metal -= custo.get("metal", 0)
            self.recursos.cristal -= custo.get("cristal", 0)
            self.recursos.prometium -= custo.get("prometium", 0)

            # Constrói ou evolui
            if not construcao.construido:
                construcao.construir()
            else:
                construcao.evoluir()

            print(f"✅ Construção processada: {construcao.nome} (nível {construcao.nivel})")
            self.fila_construcoes.pop(0)
        else:
            print(f"⚠️ Recursos insuficientes para {construcao.nome}. Aguardando...")

    def processar_fila_pesquisas(self):
        """
        Processa a próxima ordem de pesquisa da fila, se houver recursos disponíveis.
        """
        if not self.fila_pesquisas:
            return

        tecnologia = self.fila_pesquisas[0]

        if tecnologia.pesquisada:
            print(f"ℹ️ Tecnologia {tecnologia.nome} já foi pesquisada.")
            self.fila_pesquisas.pop(0)
            return

        custo = tecnologia.custo()

        if (self.recursos.metal >= custo.get("metal", 0) and
            self.recursos.cristal >= custo.get("cristal", 0) and
            self.recursos.prometium >= custo.get("prometium", 0)):

            # Desconta recursos
            self.recursos.metal -= custo.get("metal", 0)
            self.recursos.cristal -= custo.get("cristal", 0)
            self.recursos.prometium -= custo.get("prometium", 0)

            tecnologia.pesquisada = True
            print(f"✅ Pesquisa concluída: {tecnologia.nome}")
            self.fila_pesquisas.pop(0)
        else:
            print(f"⚠️ Recursos insuficientes para pesquisar {tecnologia.nome}. Aguardando...")

    def processar_tick(self):
        """
        Executa o ciclo do tick.
        Por enquanto, apenas produz recursos com base nas construções e tecnologias.
        """
        print(f"🎯 Tick iniciado para o planeta {self.planeta.nome}")
        self.atualizar_recursos()
        print(f"✅ Tick finalizado. Recursos: Metal={self.recursos.metal}, Cristal={self.recursos.cristal}, Prometium={self.recursos.prometium}\n")