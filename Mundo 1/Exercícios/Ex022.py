# n = input("Digite seu nome: ")
# n = str(input("Digite seu nome: ")).strip()
# print(f"Em maiúsculo: {n.upper()}\nEm minúsculo: {n.lower()}")
# ns = len(n) - n.count(" ")
# print(f"Seu nome possui {ns} letras")
# print(f"O primeiro nome possui {len(n.split()[0])} letras")
# -------------------------------------------------------------------
import emoji
n = input("Digite seu nome: ")
print(emoji.emojize(f"Seu nome escrito em letras maiúsculas fica \033[4:31m{n.upper()}\033[m"
                    f" :pencil:"
                    f"\nSeu nome escrito em letras minúsculas fica: \033[4:32m{n.lower()}\033[m"
                    f" :memo:"
                    f"\nSeu nome completo possui \033[4:33m{len(n) - n.count(' ')} letras\033[m"
                    f" :bookmark:"
                    f"\nSeu primeiro nome possui \033[4:34m{len(n.split()[0])} letras\033[m"
                    f" :bookmark:",
                    use_aliases=True))
# Pesquisar o primeiro espaço indicaria a quantidade de letras do primeiro nome
