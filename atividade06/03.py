"""
Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP. 
O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.

"""
import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    try:
        response.raise_for_status()  
        dados = response.json()

        if "erro" in dados:
            return "CEP não foi encontrado"
        return f""" 
        CEP: {dados['cep']}
        Logradouro: {dados['logradouro']}
        Bairro: {dados['bairro']}
        Cidade: {dados['localidade']}
        Estado: {dados['estado']}
        """
    
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro na consulta: {e}")

cep = input("Digite um CEP para consulta (somente números): ")
print("\nConsultando CEP...")
resultado = consultar_cep(cep)

print(resultado)