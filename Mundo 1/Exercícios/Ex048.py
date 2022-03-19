from emoji import emojize
print("\n" + "="*6, emojize(":crystal_ball: CALCULADORA MÁGICA :crystal_ball:", use_aliases=True), "="*6)
s = 0  # acumulador
for c in range(1, 501):  # for c in range(1, 501, 2):
    if c % 3 == 0 and c % 2 == 1:
        s += c
print("\nA soma dos números ímpares que\nsão múltiplos de 3 entre 1\ne 500 é: {}".format(s))
