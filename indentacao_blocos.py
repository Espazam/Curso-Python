def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")
        print("Retire o seu dinheiro no caixa.")
    
    if saldo < valor:
        print("Saldo Insuficiente")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")



sacar(1000)