"""
2- Classificador de Idade


Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

Criança (0-12 anos),

Adolescente (13-17 anos),

Adulto (18-59 anos)

Idoso (60 anos ou mais).

"""

idade = int(input("Insira a sua idade: "))

if idade < 0:
    print("VALOR INVÁLIDO, insira um valor positivo")
elif idade >= 0 and idade <= 12: 
    print("Você é uma criança")
elif idade >= 13 and idade <= 17:
    print("Você é um adolescente")
elif idade >= 18 and idade <= 59:
    print("Você é um adulto")
else: 
    print("Você é um idoso")