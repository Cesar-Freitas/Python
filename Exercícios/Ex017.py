# import math
# import emoji
# print(emoji.emojize("      :triangular_ruler: CALCULADORA DE PIÁGORAS :triangular_ruler: ",
#                    use_aliases=True))
# print("="*40)
# ca = float(input("DIGITE O VALOR DO CATETO ADJACENTE: "))
# co = float(input("DIGITE O VALOR DO CATETO OPOSTO: "))
# h = math.hypot(co, ca)
# print("-"*40)
# print("A hipotenusa vale aproximadamente {:.2f}.".format(h))
# print("-"*40)
# print(emoji.emojize(f"A hipotenusa vale aproximadamente {math.hypot(co, ca):.2f} :books:",
#                   use_aliases=True))
# ------------------------------------------------------------------------------------------------
from math import sqrt
import emoji
print(emoji.emojize(" \033[1:32m :triangular_ruler: :blue_book: \033[m "
                    "CALCULADORA DE PITÁGORAS \033[1:32m :blue_book: :triangular_ruler: \033[m",
                    use_aliases=True))
print("="*40)
ca = float(input("DIGITE O VALOR DO CATETO ADJACENTE: "))
co = float(input("DIGITE O VALOR DO CATETO OPOSTO: "))
print("-"*40)
print(f"\033[4:34m A hipotenusa vale aproximadamente {sqrt(ca**2 + co**2):.2f}\033[m")
''' Poderíamos ter utilizado hip = sqrt(co² + ca²)'''
