print("="*39, "\n{:^39}\n".format("TABUADA") + "="*39)
n = int(input("VOCÊ QUER VER A TABUADA DO NÚMERO: "))
for c in range(0, 11):
    print(" "*9 + "-"*25)
    print(" "*9 + "|    {}  x {:3} = {:3}    |".format(n, c, c * n))
    if c == 10:
        print(" "*9 + "-"*25)
