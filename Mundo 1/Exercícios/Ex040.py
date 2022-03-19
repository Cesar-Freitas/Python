from emoji import emojize
print("=="*5, "SISTEMA DE NOTAS", "=="*5, "\n" + "-"*38)
n1 = float(input("DIGITE A PRIMEIRA NOTA: "))
n2 = float(input("DIGITE A SEGUNDA NOTA: "))
m = (n1 + n2)/2
if m < 5.0:
    print(emojize("Sua média foi de {}, portanto está :fire:\033[4:31mreprovado\033[m:fire:. "
                  "Não desanime, você vai conseguir na próxima!", use_aliases=True).format(m))
elif 5.0 <= m <= 6.9:
    print(emojize("Sua média foi de {}, portanto está de :muscle:\033[4:33mrecuperação\033[m:muscle:,"
          " sei que vai conseguir recuperar!", use_aliases=True).format(m))
else:
    print(emojize("Sua média foi de {}, portanto está :sparkles:\033[4:36maprovado\033[m:sparkles:, "
                  "parabéns pelo esforço!", use_aliases=True).format(m))
