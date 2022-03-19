n = int(input("Digite um número: "))
# print(f"O antecessor de seu número é {n-1:*^5} e o sucessor é {n+1}.")
# print("O antecessor de seu número é {} e seu sucessor é {}.".format(n-1, n+1))
suc = n+1
ant = n-1
print("O sucessor de seu número é \033[1:35m{}\033[m e o antecessor é \033[1:36m{}\033[m.".format(suc, ant))
