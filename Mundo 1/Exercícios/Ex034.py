from emoji import emojize
from time import sleep
print("-"*35, emojize("\n        :office: \033[4:36mEMPRESA SQUIK\033[m :office:\n", use_aliases=True) + "-"*35)
s = float(input("Digite o salário do funcionário: "))
print("Analisando a correção....")
sleep(3)
# print(f"O novo salário será de R$ {s + s * (10/100):.2f}" if s > 1250 else f"O novo salário será de R$ {s + s * (
# 15/100):.2f}")
if s > 1250:
    print(emojize(f"O novo salário será de R$ \033[33m{s + s * 0.10:.2f} :moneybag:\033[m", use_aliases=True))
else:
    print(emojize(f"O novo salário será de R$ \033[33m{s + s * 0.15:.2f} :moneybag:\033[m", use_aliases=True))
