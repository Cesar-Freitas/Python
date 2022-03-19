from emoji import emojize
print('= '*20, '\n' + emojize("{:^52}".format(":trident: AMERICANAS :trident:"), use_aliases=True), '\n' + '= '*20)
p = float(input("DIGITE O PREÇO DO PRODUTO (R$): "))
c = int(input(emojize('''QUAL SERÁ A CONDIÇÃO DE PAGAMENTO:
    [0] - À VISTA DINHEIRO/CHEQUE
    [1] - À VISTA NO CARTÃO
    [2] - EM 2X NO CARTÃO
    [3] - 3X OU MAIS NO CARTÃO
OPÇÃO: ''')))
print('-'*40)
if c == 0:
    v = p - (0.1 * p)
    print("O valor a ser pago será de R$ {:.2f}".format(v))
elif c == 1:
    v = p - (0.05 * p)
    print("O valor a ser pago será de R$ {:.2f}".format(v))
elif c == 2:
    print("O valor a ser pago será de R$ {:.2f}".format(p/2))
elif c == 3:
    parcelas = int(input("DIGITE A QUANTIDADE DE PARCELAS: "))
    v = (p + (0.2 * p))
    print("O valor a ser pago será de R$ {:.2f}, sendo divido em {} parcelas de R$ {}.".format(v, parcelas, v/parcelas))
else:
    print(emojize(":x: \033[31mOPÇÃO INCORRETA\033[m :x:", use_aliases=True))
