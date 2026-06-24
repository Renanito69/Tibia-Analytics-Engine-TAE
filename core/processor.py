import json
import shutil
import os
from core.analyzer import calcular_metricas,agrupar_loot, enriquecer_loot
from excel.excel_manager import salvar_dados, salvar_loot
from config import PASTA_PROCESSADOS


def processar_json(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)

        from datetime import datetime
        hunt_id = datetime.now().strftime("%d%m%y")
        
        metricas = calcular_metricas(dados)
        itens_loot = agrupar_loot(dados)
        itens_enriquecidos = enriquecer_loot(itens_loot)
        salvar_dados(metricas)
        salvar_loot(itens_enriquecidos, hunt_id)
        mover_para_processados(caminho)

    except Exception as e:
        print(f"[ERRO] {e}")


def mover_para_processados(caminho):
    os.makedirs(PASTA_PROCESSADOS, exist_ok=True)
    destino = os.path.join(PASTA_PROCESSADOS, os.path.basename(caminho))
    try:
        shutil.move(caminho, destino)
    except Exception as e:
        print(f"[Arquivo] O arquivo movido com sucesso!!!")
