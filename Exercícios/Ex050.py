s = 0
for c in range(1, 7):
    n = int(input("DIGITE O {}º NÚMERO: ".format(c)))
    if n % 2 == 0:
        s += n
print("A soma dos números pares digitados resulta em {}.".format(s))
