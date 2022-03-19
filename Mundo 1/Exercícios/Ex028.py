# import random
# import emoji
# print("--"*20, emoji.emojize("\n    :crystal_ball: :crystal_ball: A D V I N H A Ç Ã O "
#                             ":crystal_ball: :crystal_ball:", use_aliases=True))
# print("--"*20)
# n = random.randint(0, 5)
# n1 = int(input("Advinhe qual número o computador pensou: "))
# if n1 == n:
#    print(emoji.emojize("PARABÉNS, VOCÊ ACERTOU :sparkles::sparkles:", use_aliases=True))
# else:
#    print(emoji.emojize("VOCÊ ERROU :x:", use_aliases=True))
# -----------------------------------------------------------------------------------------------
from random import randint
from time import sleep
import emoji
print("--"*20, emoji.emojize("\n   \033[34m :crystal_ball: :crystal_ball: \033[m "
                             "\033[4:35m A D V I N H A Ç Ã O  \033[m"
                             "\033[34m :crystal_ball: :crystal_ball: \033[m", use_aliases=True))
print("--"*20)
n = int(input("Digite o número que você acha que o computador pensou: "))
print("Processando.. ")
sleep(3)
print(emoji.emojize("PARABÉNS, VOCÊ ACERTOU \033[33m :sparkles::sparkles: \033[m", use_aliases=True)
      if n == randint(0, 5) else emoji.emojize("VOCÊ ERROU \033[31m :x: \033[m",
                                               use_aliases=True))
