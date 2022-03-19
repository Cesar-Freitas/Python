n = int(input("Digite um número inteiro = "))
s = 0
if n == 1 or 2 or 3:
    print("O número {} é primo!!".format(n))
else:
    for c in range(1, 3):
        if n % 1 == 0 and n % n == 0:
            n += 1
            s += 1
    if s == 1:
        print("O número {} é primo!!".format(n))
    else:
        print("O número {} não é primo!!".format(n))


for c in range(1, 3):
    if n % 1 == 0 and n % n == 0:
        n += 1
        s += 1
if s == 1:
    print("O número {} é primo!!".format(n))
else:
    print("O número {} não é primo!!".format(n))
# -------------------------------------------------------------------------------------
# o número primo só é divisível duas vezes, por 1 e ele mesmo. Podemos colocar
# um laço de repetição e ver se o número é divisível apenas 2 vezes. Toda vez que
# ele for divisível, um contador roda.
