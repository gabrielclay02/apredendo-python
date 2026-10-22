print("calculo consumo de energia")

leitura_atual = float(input("digite a leitura atual: "))
leitura_anterior = float(input("digite a leitura anterior: "))
tarifa = float(input("digite a tarifa por kwh: "))

consumo = leitura_atual - leitura_anterior
print(f"o consumo de energia foi de {consumo} kwh")

valor_energia = consumo * tarifa
print(f"o valor da energia foi de R$ {valor_energia:.2f}")

# Corrigido o nome da variável para usar underline em vez de espaços
adicional_bandeira = (consumo / 100) * 4.75
print(f"o adicional da bandeira tarifária foi de R$ {adicional_bandeira:.2f}")

soma_parcial = valor_energia + adicional_bandeira
impostos = soma_parcial * 0.18

print(f"Impostos (18%): R$ {impostos:.2f}")

valor_total = soma_parcial + impostos
print(f"Valor total da conta: R$ {valor_total:.2f}")
