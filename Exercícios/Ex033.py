n1 = int(input("Digite o primeiro número: "))
[maior, menor] = n1, n1
n2 = int(input("Digite o segundo número: "))
if n2 > maior:
    maior = n2
else:
    if n2 < menor:
        menor = n2
n3 = int(input("Digite o terceiro número: "))
if n3 > maior:
    maior = n3
else:
    if n3 < menor:
        menor = n3
print("O \033[4:34mmaior\033[m número digitado foi o {} e o \033[4:31mmenor\033[m foi o {}.".format(maior, menor))
