print("-"*45)
n = float(input("Digite o valor em metros para ser convertido: "))
c = n*100
m = n*1000
# print(f"VALOR EM CENTÍMETROS: {c} cm\nVALOR EM MILÍMETROS: {m} mm")
print("VALOR EM CENTÍMETROS: \033[7:37:40m{:.2f}\033[m cm".format(c), end=" <===> ")
print(f"VALOR EM MILÍMETROS: \033[7:30:41m{m:.2f}\033[m mm")
