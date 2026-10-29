print("------------------------------------------------------")
print("         UNIVERSIDADE CIDADE SÃO PAULO")
print("------------------------------------------------------")
print('')
print("--------------------VERIFICAÇÃO------------------------")
print("")

qnt = int(input("Quantos alunos irá avaliar?"))
while (qnt > 0):
  aluno = input("Digite o nome do aluno: ")
  nota1 = float(input("Primeira nota: "))
  nota2 = float(input("Segunda nota: "))
  print("------------------------------------------------------")
  media = (nota1 + nota2) / 2
  print('')
  if media >= 6:
    print("-----------------STATUS---------------------")
    print(f"ALUNO: {aluno}")
    print(f"MÉDIA: {media}")
    print("  *APROVADO* ")
    print("--------------------------------------------")
  elif media < 6:
    print("-----------------STATUS---------------------")
    print(f"ALUNO: {aluno}")
    print(f"MÉDIA: {media}")
    print("  *RECUPERAÇÃO* ")
    print("--------------------------------------------")
  elif media <= 1:
    print("-----------------STATUS---------------------")
    print(f"ALUNO: {aluno}")
    print(f"MÉDIA: {media}")
    print("  *REPROVADO* ")
    print("--------------------------------------------")
    qnt -= 1