import datetime
from emoji import emojize
t = 0
hv = 0
mn = 0
print("="*5, emojize(":family: ANALISADOR DE PESSOAS :family:"), "="*5 + '\n' + '-'*39)
for c in range(1, 5):
    n = input("Digite o nome da {}ª pessoas: ".format(c))
    nc = int(input("Digite a data de nascimento da {}ª pessoa: ".format(c)))
    i = datetime.date.today().year - nc
    s = input("Digite o sexo da {}ª pessoa [M/F]: ".format(c))
    t += i
    print("-"*39)
    if s.upper() == "M" and i > hv:
        hv = i
        hmv = n
    elif s.upper() == "F" and i < 20:
        mn += 1
m = t/4
print("A média de idade é {:.2f}, {} é o homem mais velho e há {} mulher(es) com menos de 20 anos."
      .format(m, hmv, mn))
