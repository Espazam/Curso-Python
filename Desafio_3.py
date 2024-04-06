# Ler a quantidade de casos de teste
n = int(input())

# Loop para cada caso de teste
for _ in range(n):
    # Ler os valores A e B
    a, b = input().split()

    # Verificar se B corresponde aos últimos dígitos de A
    if a.endswith(b):
        print("encaixa")
    else:
        print("nao encaixa")
