import emoji
n = int(input("Digite um número: "))
# if n % 2 == 0:
#    print("O número digitado é par!")
# else:
#    print("O número digitado é ímpar!")
print(emoji.emojize("\033[36mO número é par\033[m \033[33m:sparkling_heart:\033[m" if n % 2 == 0 else
                    "\033[31mO número é ímpar :anger:\033[m", use_aliases=True))
