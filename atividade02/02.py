"""
2- Calculadora de Desconto 

Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:



Nome do produto: "Camiseta"

Preço original: R$ 50.00

Porcentagem de desconto: 20% 
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""
produto_01 = "Camiseta"
valor_produto01 = 50
desconto = 20 #Em %

valor_desconto_produto01 = valor_produto01 - valor_produto01 * desconto / 100
print(f"A {produto_01} custa {valor_produto01} reais, estamos com um desconto de {desconto}%.")
print("-" * 45)
print(f"O valor final da camiseta com o desconto aplicado fica: R${valor_desconto_produto01}")
print("-" * 45)
print(f"Sendo assim o desconto foi de: {valor_desconto_produto01} reais.")