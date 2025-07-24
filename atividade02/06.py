"""
6- Calculadora de salário por horas trabalhadas

Leia o número de um funcionário, seu número de horas trabalhadas e o valor que recebe por hora. Calcule o salário do funcionário e exiba o resultado formatado corretamente.

Entrada:

O programa recebe 2 números inteiros e 1 número com duas casas decimais, representando:


Número do funcionário (numero_funcionario).

Quantidade de horas trabalhadas (horas_trabalhadas).

Valor recebido por hora (valor_por_hora).
"""

numero_funcionario = int(input("Digite o número do funcionário: "))
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
valor_hora = float(input("Digite o valor recebido por hora trabalhada: "))

salario = horas_trabalhadas * valor_hora

print(f"O fúncionario {numero_funcionario} tem um sálario de = R$ {salario:.2f}")
print(f"Trabalhou por: {horas_trabalhadas} horas")
print(f"Recebendo R$ {valor_hora:.2f} por hora trabalhada")