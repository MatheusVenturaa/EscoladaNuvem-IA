"""
Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação).
 Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.
"""
def verificaror_palindromo(texto):
    texto = texto.lower()
    texto = ''.join(letra for letra in texto if letra.isalnum())
    
    if texto == texto[::-1]:
        return "Sim"
    else:
        return "Não"

frase = input("Digite uma palavra ou frase para fazer a verificação: ")

resultado = verificaror_palindromo(frase)

print(f"A frase {frase} é Palindromo? {resultado}")