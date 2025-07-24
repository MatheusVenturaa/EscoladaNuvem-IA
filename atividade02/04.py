"""
4- Calculadora de Consumo de Combustível

 Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:



Distância percorrida: 300 km

Combustível gasto: 25 litros 
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
"""
distancia = 300.00 #Km
combustivel = 25.00 #L

consumo = distancia / combustivel #Km/l

print(f"A distância percorrida foi de: {distancia:.2f}Km")
print(f"O combustível consumido foi: {combustivel:.0f}L")
print(f"Sendo assim o consumo médio da viagem foi de: {consumo:.2f}Km/l")
