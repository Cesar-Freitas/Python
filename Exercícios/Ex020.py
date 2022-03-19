# import emoji
# import random
# a1 = input("Digite o nome do primeiro aluno: ")
# a2 = input("Digite o nome do segundo aluno: ")
# a3 = input("Digite o nome do terceiro aluno: ")
# a4 = input("Digite o nome do quarto aluno: ")
# grupo = "a1 a2 a3 a4".split()
# random.shuffle(grupo)
# print(emoji.emojize("A ordem de apresentação será {} :revolving_hearts:".format(grupo),
# use_aliases=True))
# ----------------------------------------------------------------------------------------
import emoji
from random import sample
print(emoji.emojize("== :couple: "
                    "\033[4:30:43m SORTEIO DA APRESENTAÇÃO \033[m"
                    ":couple: ==", use_aliases=True))
print("--"*18)
a1 = input("Digite o nome do primeiro membro: ")
a2 = input("Digite o nome do segundo membro: ")
a3 = input("Digite o nome do terceiro membro: ")
a4 = input("Digite o nome do quarto membro: ")
print("--"*18, f"\nA ordem de apresentação será \033[34m {sample([a1, a2, a3, a4], k=4)} \033[m",
      end="")
print(emoji.emojize(" :two_men_holding_hands::two_women_holding_hands:", use_aliases=True))
print(emoji.emojize("\033[31m :sparkles: \033[m \033[33m :star2: \033[m"*10, use_aliases=True))
# O comando lista = [a1, a2, a3, a4] também ajudaria.
