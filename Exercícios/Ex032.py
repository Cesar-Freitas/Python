a = int(input("Digite o ano: "))
# if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
#    print("O ano de {} é bissexto!!".format(a))
# else:
#     print("O ano de {} não é bissexto!!".format(a))
print("\033[4:32mO ano de {} é bissexto!!\033[m".format(a) if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0 else
      "\033[4:31mO ano de {} não é bissexto!!\033[m".format(a))

''' 
from datetime import date
date.today().year <-- ano atual
'''