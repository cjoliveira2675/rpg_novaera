import asyncio
from datetime import datetime

from core.models.tecnologias_model import *
from core.models.constructions_model import *

class GameManager:
    def __init__(self, jogador, planeta, top_summary=None, page=None):
        self.jogador = jogador
        self.planeta = planeta
        self.page = page
        self.top_summary = top_summary
        self.recursos = planeta.recursos
        self.construcoes = planeta.construcoes
        self.tecnologias = jogador.tecnologias
        self.fila_construcoes = []
        self.fila_pesquisas = []
        self.tick_counter = 0
        self.eficiencia_atual = 1.0

    def calcular_eficiencia_energetica(self, energia_disponivel: int, energia_necessaria: int) -> float:
        if energia_necessaria <= 0:
            eficiencia = 1.0
        else:
            eficiencia = energia_disponivel / energia_necessaria
            eficiencia = max(min(eficiencia, 1.0), 0.01)  # Limita entre 1% e 100%

        self.eficiencia_atual = eficiencia
        return eficiencia

    def atualizar_recursos(self):
        """
        Produz recursos com base nas construções e tecnologias.
        Considera produção e consumo de energia.
        Aplica penalização de eficiência caso energia seja insuficiente.
        """
        producao = {"metal": 0, "cristal": 0, "prometium": 0}
        energia_disponivel = 0
        energia_necessaria = 0

        # Primeiro laço: calcular energia total disponível e necessária
        for construcao in self.construcoes:
            if not construcao.construido:
                continue

            prod = construcao.produzir()  # produção bruta
            cons = construcao.consumir()

            # Coleta energia produzida separadamente
            if "energia" in prod:
                energia_disponivel += prod["energia"]

            energia_necessaria += cons.get("energia", 0)

        # Calcular eficiência energética (mínimo 1%)
        eficiencia = self.calcular_eficiencia_energetica(energia_disponivel, energia_necessaria)

        print(f"🔍 Energia disponível: {energia_disponivel} | Necessária: {energia_necessaria}")
        print(f"📉 Eficiência energética aplicada: {round(eficiencia * 100)}%")

        # Penaliza produção apenas das construções que NÃO produzem energia
        for construcao in self.construcoes:
            if not construcao.construido:
                continue

            prod = construcao.produzir()
            if not isinstance(prod, dict):
                continue  # segurança contra erros

            # Se não produz energia, aplica penalidade
            if "energia" not in prod:
                prod = {k: int(v * eficiencia) for k, v in prod.items()}

            # Acumula produção
            for recurso, valor in prod.items():
                if recurso in producao:
                    producao[recurso] += valor
                elif recurso == "energia":
                    # já foi contabilizada no primeiro laço
                    continue

        # Aplicar bônus de tecnologias
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
                energia_necessaria += 60  # considera esse custo

            elif isinstance(tecnologia, EspecializacaoMineracao):
                for k in producao:
                    producao[k] *= 1.15
                energia_necessaria *= 1.10

        # Aplica produção nos recursos
        self.recursos.metal += int(producao["metal"])
        self.recursos.cristal += int(producao["cristal"])
        self.recursos.prometium += int(producao["prometium"])

        print(f"✅ Recursos atualizados: {producao}")

        energia_liquida = energia_disponivel - energia_necessaria
        return energia_liquida

    def processar_fila_construcoes(self):
        if not self.fila_construcoes:
            return

        construcao = self.fila_construcoes[0]

        if construcao.construido:
            custo = construcao.custo_nivel(construcao.nivel + 1)
        else:
            custo = construcao.custo_nivel(1)

        if (self.recursos.metal >= custo.get("metal", 0) and
            self.recursos.cristal >= custo.get("cristal", 0) and
            self.recursos.prometium >= custo.get("prometium", 0)):

            self.recursos.metal -= custo.get("metal", 0)
            self.recursos.cristal -= custo.get("cristal", 0)
            self.recursos.prometium -= custo.get("prometium", 0)

            if not construcao.construido:
                construcao.construir()
            else:
                construcao.evoluir()

            print(f"✅ Construção processada: {construcao.nome} (nível {construcao.nivel})")
            self.fila_construcoes.pop(0)
        else:
            print(f"⚠️ Recursos insuficientes para {construcao.nome}. Aguardando...")

    def processar_fila_pesquisas(self):
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

            self.recursos.metal -= custo.get("metal", 0)
            self.recursos.cristal -= custo.get("cristal", 0)
            self.recursos.prometium -= custo.get("prometium", 0)

            tecnologia.pesquisada = True
            print(f"✅ Pesquisa concluída: {tecnologia.nome}")
            self.fila_pesquisas.pop(0)
        else:
            print(f"⚠️ Recursos insuficientes para pesquisar {tecnologia.nome}. Aguardando...")

    def executar_acao(self, construcao, label_nivel=None):
        # Evita evoluir estruturas se eficiência energética estiver abaixo de 30%, exceto plantas solares
        energia_liquida = self.atualizar_recursos()
        if self.eficiencia_atual < 0.3 and not isinstance(construcao, PlantaSolar):
            print(f"⛔ Eficiência energética muito baixa ({round(self.eficiencia_atual * 100)}%). Construa fontes de energia antes de evoluir outras estruturas.")
            return

        if not construcao.construido:
            sucesso = construcao.construir(self.recursos.__dict__)
            if not sucesso:
                return
        else:
            sucesso = construcao.evoluir(self.recursos.__dict__)
            if not sucesso:
                return

        # Atualização da interface
        if label_nivel:
            label_nivel.value = f"Nível: {construcao.nivel}"

        if self.top_summary:
            self.top_summary.atualizar(self.recursos, energia_liquida)

        if self.page:
            self.page.update()

    async def iniciar_tick_loop(self):
        while True:
            energia_liquida = self.processar_tick()
            self.tick_counter += 1

            if self.top_summary:
                self.top_summary.atualizar(self.planeta.recursos, energia_liquida)
                self.top_summary.atualizar_tempo_e_tick(
                    datetime.now().strftime('%d/%m/%Y %H:%M'),
                    self.tick_counter
                )

            if self.page:
                self.page.update()

            await asyncio.sleep(3)
    
    def processar_tick(self):
        print(f"🎯 Tick iniciado para o planeta {self.planeta.nome}")
        energia_liquida = self.atualizar_recursos()
        print(f"✅ Tick finalizado. Recursos: Metal={self.recursos.metal}, Cristal={self.recursos.cristal}, Prometium={self.recursos.prometium}\n")
        return energia_liquida
