"""
Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.
"""
#O enunciado não especificou se seria na exata data atual, então o calculo acaba sendo baseado apenas no ano
from datetime import date
def calcular_idade_dias(ano_nascimento):
    ano_atual = date.today().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias

try:
    ano = int(input("Digite o seu ano de nascimento: ")) 
    idade_dias = calcular_idade_dias(ano)
    print(f"Você tem aproximadamente {idade_dias} dias.")

except ValueError:
    print("Entrada inválida, digite um ano válido.")