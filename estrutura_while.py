opcao = -1

while opcao !=0:
    opcao = int(input("[0] Sair \n[1] Sacar \n[2] Extrato  \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
    else:
        print("Opcao Invalida!")
else:
    print("Obrigado!")


while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)

for numero in range(100):

    if numero % 2 == 0: #apenas numeros impares
        continue 

    print(numero, end="  ")