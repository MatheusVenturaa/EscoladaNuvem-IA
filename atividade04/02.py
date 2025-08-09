"""
Crie um programa que permita a um professor registrar as notas de uma turma. 
O programa deve continuar solicitando notas até que o professor digite 'fim'. 
Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando. 
No final, deve exibir a média da turma.
"""

notas = []

print("Digite as notas dos alunos (de 0 a 10). Digite 'fim' para terminar.")

while True:
    entrada = input("Digite a próxima nota: ")

    if entrada.lower() == 'fim':
        break  
    try:
        nota = float(entrada)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'fim'.")
        continue  

    if 0 <= nota <= 10:
        notas.append(nota)
        print(f"Nota {nota} registrada com sucesso.")
    else:
        print("Nota inválida. Por favor, insira um valor entre 0 e 10.")
       
if len(notas) > 0:
    media = sum(notas) / len(notas)
    print(f"Total de notas válidas registradas: {len(notas)}")
    print(f"A média da turma é: {media:.2f}")
else:
    print("Nenhuma nota válida foi registrada. Não é possível calcular a média.")

