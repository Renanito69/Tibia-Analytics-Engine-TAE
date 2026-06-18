from api_client import buscar_item_api


def converter_numero(valor):
    try:
        return float(valor.replace(",", "").strip())
    except:
        return 0.0


def converter_tempo(tempo_str):
    tempo_str = tempo_str.replace("h", "")
    horas, minutos = map(int, tempo_str.split(":"))

    tempo_decimal = horas + minutos / 60
    tempo_excel = (horas * 60 + minutos) / (24 * 60)

    return tempo_decimal, tempo_excel


def calcular_metricas(dados):
    xp = converter_numero(dados.get("XP Gain", "0"))
    xp_h = converter_numero(dados.get("XP/h", "0"))

    loot = converter_numero(dados.get("Loot", "0"))
    supplies = converter_numero(dados.get("Supplies", "0"))
    balance = converter_numero(dados.get("Balance", "0"))

    damage = converter_numero(dados.get("Damage", "0"))
    healing = converter_numero(dados.get("Healing", "0"))

    tempo_horas, tempo_excel = converter_tempo(dados.get("Session length", "00:00h"))

    profit = loot - supplies
    profit_h = profit / tempo_horas if tempo_horas > 0 else 0

    return {
        "exp": xp,
        "exp_hora": xp_h,
        "loot": loot,
        "supplies": supplies,
        "profit": profit,
        "profit_por_hora": profit_h,
        "balance": balance,
        "damage": damage,
        "healing": healing,
        "tempo_horas": tempo_horas,  # para cálculos
        "tempo_excel": tempo_excel  # para exibição
    }
    

def agrupar_loot(dados):
    itens = dados.get("Looted Items", [])

    loot = {}

    for item in itens:
        if not isinstance(item, dict):
            continue

        nome = item.get("Name", "desconhecido")
        quantidade = item.get("Count", 0)

        # 🔥 GARANTE STRING
        if not isinstance(nome, str):
            continue

        if nome in loot:
            loot[nome] += quantidade
        else:
            loot[nome] = quantidade

    return loot


def enriquecer_loot(loot_dict):
    resultado = []

    for item, qtd in loot_dict.items():
        info = buscar_item_api(item)

        preco = info["preco"] or 0
        total = preco * qtd

        resultado.append({
            "item": item,
            "quantidade": qtd,
            "npc": info["npc"],
            "cidade": info["cidade"],
            "valor_unidade": preco,
            "valor_total": total
        })

    return resultado
