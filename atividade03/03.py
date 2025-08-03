"""
3- Calculadora de IMC


Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.


< 18.5: classificacao = "Abaixo do peso" 

< 25: classificacao = "Peso normal"

 < 30: classificacao = "Sobrepeso"

 Para os demais cenários: classificacao = "Obeso"
 """

peso = int(input("Insira o seu peso (Kg) : "))
altura = float(input("Insira a sua altura (Metros): "))

imc = peso / (altura ** altura)

if imc < 18.5:
    print("Classificação = Abaixo do peso")
elif imc < 25:
    print("Classificação = Peso normal")
elif imc < 30:
    print("Classificação = Sobrepeso")
else:
    print("Classificação = Obeso")

print(f"Seu IMC é: {imc:.1f}")