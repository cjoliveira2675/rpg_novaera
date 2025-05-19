import json
import os

def load_config(config_path='config.json'):
    """Lê o arquivo config.json e retorna o dicionário de configurações."""
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Arquivo de configuração não encontrado: {config_path}")
    
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)
    return config