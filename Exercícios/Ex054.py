from emoji import emojize
import datetime
j = 0
a = 0
for c in range(1, 8):
    y = int(input("Digite o ano de nascimento da {}ª pessoa: ".format(c)))
    if datetime.date.today().year - y < 18:
        j += 1
    else:
        a += 1
print(emojize("{} pessoas atingiram a maioridade :older_man: e {} pessoas ainda não a atingiram :baby:.".format(a, j),
      use_aliases=True))
