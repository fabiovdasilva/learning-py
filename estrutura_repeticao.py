text = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in text:
    if letra.upper() in VOGAIS:
        print(letra, end="")

else:
    print()
    print("Executar o final")

#Exemplo com range
for numero in range(0, 51, 5): #step[inico:fim:passo]
    print(numero, end=" ")

# range(4)
# range(0,4) - Não percorre lista
#
# list(range(4))
# [0, 1, 2, 3] - Percorre lista