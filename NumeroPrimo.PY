
#Identificador de Número Primo

print("==========================================")
P = int(input("Digite o Número que deseja descobrir se é um número Primo Ou não: \n Número: "))

Contagem = 0
Divisores = 0

while (P > Contagem):
    Contagem += 1
    if (P % Contagem == 0):
        Divisores += 1


print("... Calculando")
print("----------------------------")

if Divisores > 2:
    print(f"O número {P} Não é Um Número Primo !!")
else:
    print(f"O número {P} É um Número Primo !!")

print("----------------------------")