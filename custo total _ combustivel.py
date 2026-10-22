print("ola, viajante")

distancia_ida = float(input(" digite a Distância de ida (km): ").replace(',', '.'))
consumo = float(input(" digite oConsumo médio (km/l): ").replace(',', '.'))
preco_litro = float(input(" digite o Preço do litro (R$): ").replace(',', '.'))

distancia_total =distancia_ida*2
litros_necessarios= distancia_total / consumo
custo_total = litros_necessarios * preco_litro


print(f"Distância total: {distancia_total:.0f} km")
print(f"Litros: {litros_necessarios:.2f}")
print(f"Custo: R$ {custo_total:.2f}")
