import os
from watcher import iniciar_monitoramento
from config import PASTA_JSON


if __name__ == "__main__":
    os.makedirs(PASTA_JSON, exist_ok=True)
    iniciar_monitoramento(PASTA_JSON)
    