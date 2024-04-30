def sacar(valor):
    saldo=500

    if saldo >= valor:
        print(f"valor sacado: {valor}")
        print("retire o seu dinheiro!")

    print("Obrigado")

def depositar(valor):
    saldo = 500
    saldo += valor

    print(saldo)
  
depositar(500) 