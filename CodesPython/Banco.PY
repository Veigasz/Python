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
elif (Saque % 2 == 0) and (Saque % 5 == 0): 
    print("Valor Válido Para Saque!!")
else:
    print("Valor Inválido !! (Escolha um valor múltiplo de 5 e Par !!)")
    os._exit(0)

print("------------------------------------------------------")



print("Calculando Notas...")
print("...")
print("")

N100 = Saque // 100
N50 = Saque % 100 // 50
N20 = N50 % 50 // 20
N10 = N20 % 20 // 10
N5 = N10 % 10 // 5
N2 = N5 % 5 // 2

print("Relátoria de Notas: ")
print("-----------------------------")
print("")
print(f"*Notas de 100: {N100} ") 
print(f"*Notas de 50: {N50}" )
print(f"*Notas de 20: {N20}") 
print(f"*Notas de 10: {N10}")
print(f"*Notas de 5: {N5}")