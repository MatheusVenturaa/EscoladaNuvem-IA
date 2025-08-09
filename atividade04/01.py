"""
Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição, subtração, multiplicação e divisão) entre dois números. 
A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação. Siga as especificações abaixo:

A calculadora deve solicitar ao usuário que insira dois números e uma operação.

As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).

O programa deve continuar solicitando entradas até que uma operação válida seja concluída.

Trate os seguintes erros:

Entrada inválida (não numérica) para os números

Divisão por zero

Operação inválida"""


while True:
   
    numero1 = input("Digite o primeiro número: ")
    numero2 = input("Digite o segundo número: ")

   
    try:
        num1 = float(numero1)
        num2 = float(numero2)
    except ValueError:
       
        print("\nErro: Por favor, digite apenas números.")
        print("Vamos tentar de novo.\n")
        continue  

    
    operacao = input("Digite a operação (+, -, *, /): ")

    
    resultado = None  

    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        
        if num2 == 0:
            print("\nErro: Divisão por zero não é permitida.")
            print("Vamos tentar de novo.\n")
            continue  
        else:
            resultado = num1 / num2
    else:
        
        print("\nErro: Operação inválida. Use apenas '+', '-', '*' ou '/'.")
        print("Vamos tentar de novo.\n")
        continue  

   
    print(f"\nO resultado de {num1} {operacao} {num2} é: {resultado:.2f}")
    break 