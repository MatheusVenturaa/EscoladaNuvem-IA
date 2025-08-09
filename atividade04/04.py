"""
Crie um programa que solicite ao usuário que insira números inteiros. O programa deve continuar solicitando números até que o usuário digite 'fim'.
Para cada número inserido, o programa deve informar se é par ou ímpar. 
Se o usuário inserir algo que não seja um número inteiro, o programa deve
informar o erro e continuar. No final, o programa deve exibir a quantidade de números pares e ímpares inseridos.
"""
numeros_pares = 0
numeros_impares = 0

print("Digite números inteiros. Para encerrar, digite 'fim'.")


while True:
    entrada = input("\nDigite um número: ")

    if entrada.lower() == 'fim':
        print("\nEncerrando o programa...")
        break 

  
    try:
        numero = int(entrada)

        if numero % 2 == 0:
            print(f"O número {numero} é PAR.")
            numeros_pares += 1 
        else:
            print(f"O número {numero} é ÍMPAR.")
            numeros_impares += 1 

    except ValueError:

        print("Erro: Por favor, insira apenas um número inteiro válido.")
        continue 

print(f"Quantidade de números pares inseridos: {numeros_pares}")
print(f"Quantidade de números ímpares inseridos: {numeros_impares}")