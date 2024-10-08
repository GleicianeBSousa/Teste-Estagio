
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total = sum(faturamento_estados.values())

for estado, faturamento in faturamento_estados.items():
    print(f"{estado}: {faturamento / faturamento_total:.0%} do faturamento total.")