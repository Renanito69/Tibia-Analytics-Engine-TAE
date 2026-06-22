try:
    from watcher import iniciar_monitoramento
    from config import PASTA_JSON

except ModuleNotFoundError:
    from dependencias import instalar_dependencias

    instalar_dependencias()

    print("Dependências instaladas. Reinicie o programa.")
    exit()

import os

if __name__ == "__main__":
    os.makedirs(PASTA_JSON, exist_ok=True)
    iniciar_monitoramento(PASTA_JSON)