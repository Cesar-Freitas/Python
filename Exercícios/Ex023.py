# print("--"*21)
# n = input("Digite um número entre 0000 e 9999: ")
# print(f"UNIDADE: {n[3]}\nDEZENA: {n[2]}\nCENTENA: {n[1]}\nMILHAR: {n[0]}")
# --------------------------------------------------------------------------
print("--"*21)
n = int(input("Digite um número entre 0000 e 9999: "))
# poderia passar a variável para a classe str e usar o [n] - mostrar um caractere da str
print(f"\033[36mMILHAR:\033[m {n//1000}"
      f"\n\033[35mCENTENA:\033[m {n%1000//100}"
      f"\n\033[34mDEZENA:\033[m {(n%100)//10}"
      f"\n\033[33mUNIDADE:\033[m {n%10}")
