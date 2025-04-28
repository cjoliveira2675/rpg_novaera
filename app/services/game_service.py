# app/services/game_service.py

from app.database.db import get_connection

class GameService:
    def __init__(self):
        self.conn = get_connection()

    def process_tick(self):
        """Chama a procedure no banco para avançar o tick e atualizar o jogo."""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("CALL process_tick()")
                self.conn.commit()
            print("Tick processado com sucesso!")
        except Exception as e:
            print(f"Erro ao processar tick: {e}")

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
