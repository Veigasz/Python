#--------------Projeto de Caixa Eletronico-----------

import os

print("====================================================")
print("                CAIXA ELETRONICO")
print("====================================================")
print("")

Saldo = int(input("Digite seu Saldo total de sua Conta Bancária:\n R$"))
Saque = int(input("Digite o Valor que deseja Sacar da sua Conta:\n R$"))

if (Saque > Saldo):
    print("Valor Insufiente em Sua conta bancária !! ")
    os._exit(0)
elif (Saque % 2 == 0) or (Saque % 5 == 0): 
    print("Valor Válido Para Saque!!")
    SaldoFinal = Saldo - Saque
else:
    print("Valor Inválido !! (Escolha um valor múltiplo de 5 e Par !!)")
    os._exit(0)

print("------------------------------------------------------")



print("Calculando Notas...")
print("...")
print("")

N100 = Saque // 100
Saque = Saque % 100

N50 = Saque // 50
Saque = Saque % 50

N20 = Saque // 20
Saque = Saque % 20

N10 = Saque // 10
Saque = Saque % 10

N5 = Saque// 5
Saque = Saque % 5

N2 = Saque // 2


print("Relátoria de Notas: ")
print("-----------------------------")
print("")

if (N100 > 0):
    print(f"{N100} *Notas de 100  ") 
if (N50 > 0):
    print(f"{N50} *Notas de 50" )
if (N20 > 0): 
    print(f"{N20} *Notas de 20") 
if (N10 > 0):
    print(f"{N10} *Notas de 10")
if (N5 > 0):
    print(f"{N5} *Notas de 5")
if (N2 > 0):
    print(f"{N2} *Notas de 2")
print("-----------------------------")
print(f"Seu Saldo Atual é de: {SaldoFinal}")