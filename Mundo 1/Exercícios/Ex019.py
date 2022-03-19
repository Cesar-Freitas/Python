# import random
# import emoji
# a1 = input("Digite o nome do primeiro aluno: ")
# a2 = input("Digite o nome do segundo aluno: ")
# a3 = input("Digite o nome do terceiro aluno: ")
# a4 = input("Digite o nome do quarto aluno: ")
# print(emoji.emojize(f"{random.choice([a1, a2, a3, a4])} será o(a) aluno(a) escolhido(a) :boy: :girl:",
#                    use_aliases=True))
# Podemos criar uma lista por meio de lista = [a1, a2, a3, a4]
# ------------------------------------------------------------------------------------------------------
import emoji
from random import choice
print(emoji.emojize("\033[33m :sparkles: :sparkles: \033[m "
                    "\033[4:36m SORTEIO DE ALUNOS \033[m"
                    "\033[33m :sparkles: :sparkles: \033[m", use_aliases=True))
print("\033[31m--\033[m"*16)
a1 = input("Digite o nome do primeiro aluno: ")
a2 = input("Digite o nome do segundo aluno: ")
a3 = input("Digite o nome do terceiro aluno: ")
a4 = input("Digite o nome do quarto aluno: ")
print("--"*16)
print(emoji.emojize(f"O(a) aluno(a) escolhido será.... {choice([a1, a2, a3, a4])} "
                    f"\033[33m :star2::star2: \033[m",
                    use_aliases=True))
