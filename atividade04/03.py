"""
Crie um programa que verifique se uma senha é forte. 
Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. 
O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.
"""

print("Uma senha forte deve ter no mínimo 8 caracteres e conter pelo menos um número.")
print("Digite 'sair' a qualquer momento para encerrar o programa.")

while True:
    senha = input("\nCrie uma senha: ")

    if senha.lower() == 'sair':
        print("Programa encerrado.")
        break
    caracteres8 = len(senha) >= 8
    umnumero = False

    for caractere in senha:
        if caractere.isdigit():
            umnumero = True
            break

    if caracteres8 and umnumero:
        print("Senha forte criada com sucesso!")
        break  
    else:
        print("Senha fraca, Tente novamente.")
        if not caracteres8:
            print("- Sua senha precisa ter no mínimo 8 caracteres.")
        if not umnumero:
            print("- Sua senha precisa conter pelo menos um número.")
