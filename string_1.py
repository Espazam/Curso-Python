# Métodos Úteis da Classe String.

nome = "WeSlEy"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "   Olá mundo!   "

print(texto + ".")
print(texto.strip() + ".")
print(texto.lstrip() + ".")
print(texto.rstrip() + ".")

menu = "Python"

print("####" + menu + "####") 
print(menu.center(14))
print(menu.center(20, "#"))

print("P-y-t-h-o-n")
print("-".join(menu))