import os
PASTA_JSON = r"C:\Users\renan\AppData\Local\Tibia\packages\Tibia\log"
PASTA_PROCESSADOS = "processados"
ARQUIVO_EXCEL = "dados_hunts.xlsx"
PASTA_DADOS = "data"

os.makedirs(PASTA_DADOS, exist_ok=True)

ARQUIVO_EXCEL = os.path.join(
    PASTA_DADOS,
    "dados_hunts.xlsx"
)
