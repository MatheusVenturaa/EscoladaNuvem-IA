'''
Calculadora de Número Inteiro
Leia quatro valores inteiros A, B, C e D. 
A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).
Entrada: O arquivo de entrada contém 4 valores inteiros. 
Saída: Imprima a mensagem "DIFERENCA = " com todas as letras maiúsculas.
'''
valor_a = int(input("Digite o valor de A : "))
valor_b = int(input("Digite o valor de B : "))
valor_c = int(input("Digite o valor de C : "))
valor_d = int(input("Digite o valor de D : "))

diferenca = valor_a * valor_b - valor_c * valor_d
print("A fórmula para a diferença é (A * B - C * D)")
print(
    "E a diferença seguindo a fórmula e utilizando os valores fornecidos" 
    f" (A= {valor_a} B= {valor_b} C= {valor_c} D= {valor_d}) \n"
    f"resulta na DIFERENCA: {diferenca}")