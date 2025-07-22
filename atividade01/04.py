''''
Calculadora de Preço Total

Desenvolva um programa que calcule o preço total de uma compra. Use as seguintes informações:

Nome do produto: "Cadeira Infantil"
Preço unitário: R$ 12.40
Quantidade: 3 
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.
'''

print("Cadeira Infatil ----- R$12.40")
preco = 12.40

#Só vai aceitar valores inteiros, pois não tem como comprar meia cadeira 
quantidade = int(input("Qual a quantidade do produto que você quer: "))

valor = quantidade * preco
print (f"Certo, o valor total será de {valor}")