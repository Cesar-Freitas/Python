n = int(input("Digite um número: "))
# d = 2*n
# t = 3*n
# r = int(n**(1/2))
# print(f"O dobro de seu número é {d}, o triplo é {t} e a raiz quadrada é {r}.")
# --------------------------------------
# print(f"O dobro é {2*n}\nO triplo é {3*n}\nA raiz quadrada é {int(n**(1/2))}")
# --------------------------------------
print("O triplo é \033[4:32m{}\033[m".format(3*n), end=" >>> ")
print("O dobro é \033[4:33m{}\033[m".format(2*n), end=" >>> ")
print("A raiz quadrada é \033[4:34m{:.2f}\033[m".format(n**(1/2)))
