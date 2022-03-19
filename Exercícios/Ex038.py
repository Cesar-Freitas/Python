n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if n1 > n2:
    print("\033[33mO primeiro número é maior do que o segundo.")
elif n2 > n1:
    print("\033[35mO segundo número é maior do que o primeiro.")
else:
    print("\033[32mNão existe maior, os dois são iguais.")
