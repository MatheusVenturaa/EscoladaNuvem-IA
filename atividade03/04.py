"""
4- Conversor de Temperatura 

Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 

O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

"""

temperatura = float(input("Insira uma temperatura: "))

origem = (input("Insira a unidade de origem (C, F, K): "))
destino = (input("Insira a unidade de destino (C, F, K): "))

if origem == destino:
    resultado = temperatura 

elif origem == "C": 
    if destino == "F": #Celsius para Fahrenhehit
        resultado = (temperatura * 9/5) + 32
    else: #Celsius para Kelvin
        resultado = temperatura + 273.15

elif origem == "F": 
    if destino == "C": #Fahrenhehit para Celsius
        resultado = (temperatura - 32) * 5/9
    else: #Fahrenhehit para Kelvin
        resultado = (temperatura - 32) * 5/9 + 273.15

elif origem == "K":
    if destino == "C": #Kelvin para Celsius
        resultado = temperatura - 273.15
    else: 
        resultado = (temperatura - 273.15) * 9/5 + 32

print(f"A temperatura inicial foi {origem} e convertendo para {destino} temos o resultado de: {resultado:.2f}{destino}")
