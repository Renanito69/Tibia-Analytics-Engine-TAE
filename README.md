# Ola o projeto TAE (Tibia Abalytics Engine) e um projeto de analise de dados do hunt analyzer do tibia
oque ele faz?
ele pega o os dados e coloca na ordem 
## data/ex/loot/proft/tempo/xpHora
- DATA == Ele pega o dia do import 
- XP == Pega o xp total farmado enquanto jogava
- LOOT == Pega o total de loot que foi coletado
- PROFIT == Calcula o quanto que ganhou (loot - gastos)
- TEMPO == Mostra quanto tempo voce ficou na hunt/jogando
- XPHora == Mosta quanto de xp vc fazia por hora

Com isso ele cria outra tabela com
## balance/totalFarmado/tempoTotal/xpTotal
- balance == Ele calcula o quanto voce farmou e pode gastar (estou procurando um jeito de aprimorar)
- totalFarmado == Ele pega o total farmado no bruto sem as dispesas
- tempoTotal == Isso pega o total de tempo jogado
- xpTotal == Pega o total de xp ganho durante as hunts
