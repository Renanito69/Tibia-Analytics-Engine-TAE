import os
import time

def esperar_arquivo_pronto(caminho):
    tamanho_anterior = -1

    while True:
        tamanho_atual = os.path.getsize(caminho)

        if tamanho_atual == tamanho_anterior:
            return True

        tamanho_anterior = tamanho_atual
        time.sleep(1)