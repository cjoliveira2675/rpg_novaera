import mysql.connector

# Configurações de conexão
config = {
    'user': 'root',
    'password': 'Cosj2675@',
    'host': 'localhost',
    'database': 'rpg_novaera',
}

def produzir_recursos(planeta_id, metal, cristal, combustivel, energia):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        update_query = """
        UPDATE planetas
        SET recurso_metal = recurso_metal + %s,
            recurso_cristal = recurso_cristal + %s,
            recurso_combustivel = recurso_combustivel + %s,
            recurso_energia = recurso_energia + %s
        WHERE id = %s
        """
        cursor.execute(update_query, (metal, cristal, combustivel, energia, planeta_id))
        conn.commit()
        print(f"Recursos do planeta {planeta_id} atualizados com sucesso.")

    except mysql.connector.Error as err:
        print(f"Erro: {err}")

    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    planeta_id = 1  # Planeta Azul que inserimos no banco
    # Simulando produção neste tick
    produzir_recursos(planeta_id, metal=10, cristal=5, combustivel=3, energia=2)