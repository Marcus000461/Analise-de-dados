## Criar um programa que receba as notas dos alunos e calcule a média.
notas = []
while True:
    resposta = input("Você quer adicionar uma nota? (s/n): ")
    if resposta.lower() == "s":
        nota = float(input("Digite a nota do aluno: "))
        print("Nota adicionada:", nota)
        notas.append(nota)
    elif resposta.lower() == "n":
        break
    else:
        print("Resposta inválida. Por favor, digite 's' ou 'n'.")

soma = sum(notas)
media = soma / len(notas) if notas else 0
print(f"A média das notas é: {media:.2f}")
