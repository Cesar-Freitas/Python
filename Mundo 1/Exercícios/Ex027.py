import emoji
n = input("Digite o nome completo de uma pessoa: ").strip()
ni = n.split()[0]
nf = n.rsplit()[len(n.split()) - 1]
print(emoji.emojize(f"PRIMEIRO NOME: {ni} \033[32m :collision: \033[m "
                    f"\nÚLTIMO NOME: {nf} \033[35m :fire: \033[m", use_aliases=True))
