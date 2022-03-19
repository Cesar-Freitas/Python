# -----------------------------------------
#
n = input("Digite seu nome: ")
print("Bem vindo {}!!".format(n))
# print("Bem vindo {:10}!!".format(n))
# print("Bem vindo {:<10}!!".format(n))
# print("Bem vindo {:>10}!!".format(n))
# print(f"Bem vindo {n:=^10}!!")
# -----------------------------------------
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
div = (n1 / n2)
p = n1*n2
print(f"A divisão entre {n1} e {n2} resulta em {div:.3f}", end=" >>> ")
print("A soma entre {} e {} resulta em {}.\nO produto entre {} e {} "
      "resulta em {}".format(n1, n2, (n1+n2), n1, n2, p))
# -----------------------------------------
