
import json


with open('faturamento.json', 'r') as file:
    faturamento_diario = [dia["valor"] for dia in json.load(file)["faturamento_diario"] if dia["valor"] > 0]


menor_faturamento, maior_faturamento = min(faturamento_diario), max(faturamento_diario)
media_faturamento = sum(faturamento_diario) / len(faturamento_diario)
dias_acima_da_media = sum(1 for valor in faturamento_diario if valor > media_faturamento)


print(f"Menor valor de faturamento: R${menor_faturamento:.0f}")
print(f"Maior valor de faturamento: R${maior_faturamento:.0f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
