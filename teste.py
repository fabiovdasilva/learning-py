def palindromos(lista_strings):
    palindromo = []
    for palavra in lista_strings:
        if palavra == palavra[::-1]:
            palindromo.append(palavra)
    return palindromo

# Exemplo de uso:
lista_palavras = ["arara", "banana", "radar", "python", "asa"]
print("Palíndromos na lista:", palindromos(lista_palavras))
