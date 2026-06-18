import requests
import time
from urllib.parse import quote

BASE_URL = "https://tibiadata.bytewizards.de/"
_cache = {}

def normalizar_nome(nome):
    nome = nome.lower().strip()
    
    if nome.startswith(("a ", "an ")):
        nome = nome.split(" ", 1)[1]
    
    return nome

def buscar_item_api(nome_item):
    nome_normal = normalizar_nome(nome_item)
    print(f"Buscando '{nome_normal}' na API...")
    
    if nome_normal in _cache:
        return _cache[nome_normal]

    url = f"{BASE_URL}api/v1/items/{quote(nome_normal)}"

    try:
        resp = requests.get(url, timeout=5)

        if resp.status_code != 200:
            print(f"[API ERRO] {nome_item} - Status: {resp.status_code}")
            return {"npc": None, "cidade": None, "preco": 0}

        if not resp.text.strip():
            print(f"[API VAZIA] {nome_item}")
            return {"npc": None, "cidade": None, "preco": 0}

        data = resp.json()

        valor = int(data.get("npcValue", "0"))

        attrs = data.get("additionalAttributes", {}).get("entries", [])

        npc = "Desconhecido"
        cidade = "Desconhecido"

        for attr in attrs:
            if attr.get("key") == "sellTo":
                npc = attr.get("value", "").split(";")[0]

        resultado = {
            "npc": npc,
            "cidade": cidade,
            "preco": valor
        }

        _cache[nome_normal] = resultado
        time.sleep(0.2)

        return resultado

    except Exception as e:
        print(f"Erro ao buscar item '{nome_item}': {e}")
        return {
            "npc": "Desconhecido",
            "cidade": "Desconhecido",
            "preco": 0
        }