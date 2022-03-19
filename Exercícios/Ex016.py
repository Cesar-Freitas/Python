from math import trunc
import emoji
n = float(input("Digite um número decimal: "))
# print(emoji.emojize(f"A parte real do número {n} é {trunc(n)} :books:.", use_aliases=True))
# int(n) também serviria
r = trunc(n)
print(emoji.emojize("O número {} tem {} como parte inteira \033[7:40:32m :heavy_check_mark: \033[m".format(n, r),
                    use_aliases=True))
