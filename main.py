import os
from watcher import iniciar_monitoramento
from config import PASTA_JSON
from depedencias import instalar_dependencias

try:
    if __name__ == "__main__":
        os.makedirs(PASTA_JSON, exist_ok=True)
        iniciar_monitoramento(PASTA_JSON)
except Exception as e:
    instalar_dependencias()
    print(f"Dependências instaladas. Por favor, reinicie o programa.")