"""
Crie um programa que receba o preço original de um produto e um percentual de desconto, 
realizando o cálculo do preço final após a aplicação do desconto. 
Requisitos:
Permitir que o usuário informe o preço do produto e o percentual de desconto.
Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
Exibir o preço final com duas casas decimais para garantir precisão. 
Entrada esperada: preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10).

"""
def calcular_precofinal():

  try:
    preco_original_str = input("Digite o preço original do produto : ")
    percentual_desconto_str = input("Digite o percentual de desconto : ")

    preco_original = float(preco_original_str)
    percentual_desconto = float(percentual_desconto_str)

    if preco_original < 0 or percentual_desconto < 0:
      print("\nErro: O preço e o desconto não podem ser valores negativos.")
      return

    valor_do_desconto = preco_original * (percentual_desconto / 100)

    preco_final = preco_original - valor_do_desconto

    print(f"Preço Original: R$ {preco_original:.2f}")
    print(f"Desconto de {percentual_desconto}%: R$ {valor_do_desconto:.2f}")
    print(f"Preço Final com Desconto: R$ {preco_final:.2f}")

  except ValueError:
    print("\nErro: Entrada inválida. Por favor, insira apenas números.")
  except Exception as e:
    print(f"\nOcorreu um erro inesperado: {e}")

if __name__ == "__main__":
  calcular_precofinal()