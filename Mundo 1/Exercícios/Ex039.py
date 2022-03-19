from datetime import date
from emoji import emojize

a = date.today().year
print("X" * 10, emojize(":pencil: SISTEMA DE ALISTAMENTO :pencil:", use_aliases=True), "X" * 10)
nome = input("DIGITE SEU NOME: ")
n = int(input("DIGITE SEU ANO DE NASCIMENTO: "))
s = input("DIGITE SEU SEXO [M/F]: ")
print("x" * 50, "\n")
if s == "M":
    print("Você possui {} anos, ".format(a - n), end='')
    if a - n < 18:
        print("\033[1:36mestá muito jovem\033[m para se alistar, falta(m) {} ano(s) para seu alistamento!!"
              .format(18 - (a - n)))
    elif a - n == 18:
        print("\033[1:32mestá na hora\033[m do seu alistamento soldado!!")
    else:
        print("já passou da hora de se alistar, você está {} ano(s) \033[1:31matrasado(s)\033[m.".format((a - n) - 18))
elif s == "F":
    print("Infelizmente não é possível realizar o alistamento.")
else:
    print(emojize("OPÇÃO INVÁLIDA :x:", use_aliases=True))
