menor = 10000000000
maior = 0
for c in range(1, 6):
    m = float(input("Digite a massa da {}ª pessoa: ".format(c)))
    # if c == 1:
    # maior = m
    # menor = m
    if m > maior:
        maior = m
    elif m < menor:
        menor = m
print("A maior massa é de {} kg e a menor é de {} kg.".format(maior, menor))

''' * menor = 0 -> primeira ocorrência será menor e maior ao mesmo tempo '''
