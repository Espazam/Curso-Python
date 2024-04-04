Maior_Idade = 18
Idade_Especial = 17

idade = int(input("Informe a sua idade: "))

if idade >= Maior_Idade:
    print("Maior de idade, pode tirar a CNH.")

if idade < Maior_Idade:
    print("Ainda não possui idade mínima para tirar a CNH")


if idade >= Maior_Idade:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Ainda não possui idade mínima para tirar a CNH")


if idade >= Maior_Idade:
    print("Maior de idade, pode tirar a CNH.")
elif idade == Idade_Especial:
    print("Pode fazer aulas teóricas, mas não pode fazer as aulas práricas.")
else:
    print("Ainda não possui idade mínima para tirar a CNH")