from datetime import date
from emoji import emojize

print("=" * 60)
print(emojize(":swimmer: " * 5, use_aliases=True), "CONFEDERAÇÃO NACIONAL DE NATAÇÃO",
      emojize(":swimmer: " * 5, use_aliases=True))
print("=" * 60)
n = input("DIGITE SEU PRIMEIRO NOME: ")
y = int(input("DIGITE SEU ANO DE NASCIMENTO: "))
i = date.today().year - y
if i <= 9:
    # MIRIM
    print("{}, você está na categoria MIRIM!".format(n))
elif 9 < i <= 14:  # i <= 14
    # INFANTIL
    print("{}, você está na categoria INFANTIL!".format(n))
elif 14 < i <= 19:  # i <= 19
    # JÚNIOR
    print("{}, você está na categoria JÚNIOR!".format(n))
elif 19 < i <= 20:  # i <= 20
    # SÊNIOR
    print("{}, você está na categoria SÊNIOR!".format(n))
else:
    # MASTER
    print("{}, você está na categoria MASTER!".format(n))
print("-" * 60)
