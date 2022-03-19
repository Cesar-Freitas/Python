import emoji
n = input("Digite um nome: ").strip()
print(emoji.emojize(f"\033[4:35m{n.upper()}\033[m possui 'SILVA'? {'SILVA' in n.upper()} "
                    f"\033[32m:fireworks:\033[m", use_aliases=True))
