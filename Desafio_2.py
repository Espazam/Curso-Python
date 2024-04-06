# Dicionário com os meses do ano em inglês
meses = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

# Ler o valor inteiro entre 1 e 12
numero_mes = int(input())

# Verificar se o número está dentro do intervalo válido
if 1 <= numero_mes <= 12:
    # Imprimir o nome do mês correspondente em inglês com a primeira letra maiúscula
    print(meses[numero_mes])
else:
    print("Valor inválido. Digite um número entre 1 e 12.")
