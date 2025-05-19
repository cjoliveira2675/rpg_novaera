# app/services/game_service.py

from app.database.db import get_connection

class GameService:
    def __init__(self):
        self.conn = get_connection()

    def process_tick(self):
        """Chama a procedure no banco para avançar o tick e atualizar o jogo."""
        try:
            with self.conn.cursor() as cursor:
                # Chamada da procedure que processa o tick
                cursor.execute("CALL process_tick()")

                # Registro de log do tick (ajustar tick_id futuramente)
                cursor.execute("""
                    INSERT INTO logs_tick (tick_id, jogador_id, acao, detalhes)
                    VALUES (%s, %s, %s, %s)
                """, (1, None, "tick_manual", "Tick executado manualmente via GameService"))

                self.conn.commit()
            print("✅ Tick processado e log registrado com sucesso!")
        except Exception as e:
            print(f"❌ Erro ao processar tick: {e}")

    def get_planets(self):
        """Retorna a lista de planetas e seus dados."""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT * FROM planetas")
                planets = cursor.fetchall()
            return planets
        except Exception as e:
            print(f"Erro ao buscar planetas: {e}")
            return []

    def close(self):
        self.conn.close()
