# import emoji
# import math
# print(emoji.emojize(" :triangular_ruler: :books: CALCULADORA TRIGONOMÉTRICA", use_aliases=True), end="")
# print(emoji.emojize(" :books: :triangular_ruler: ", use_aliases=True))
# print("="*39)
# a = float(input("DIGITE O VALOR DO ÂNGULO: "))
# print("SENO: {:.2f}\nCOSSENO: {:.2f}\nTANGENTE: {:.2f}".format(math.sin(a), math.cos(a), math.tan(a)))
# print(f"SENO: {math.sin(math.radians(a)):.2f}\nCOSSENO: {math.cos(math.radians(a)):.2f}\n"
#      f"TANGENTE: {math.tan(math.radians(a)):.2f}")
# ------------------------------------------------------------------------------------------------------
from math import sin, cos, tan, radians
import emoji
print(emoji.emojize("\033[4:35m :computer: :books: :triangular_ruler:\033[m "
                    "\033[41:34m CALCULADORA TRIGONOMÉTRICA \033[m",
                    use_aliases=True), end="")
print(emoji.emojize("\033[4:35m :triangular_ruler: :books: :computer:\033[m", use_aliases=True))
print("\033[36m=\033[m"*43)
a = float(input("Digite o valor do ângulo: "))
print(f"Para um ângulo de {a}º temos os seguintes valores para seno, cosseno e tangente:\n"
      f"\033[4:35mSENO: {sin(radians(a)):.2f}\033[m"
      f"\n\033[7:35:43mCOSSENO: {cos(radians(a)):.2f}\033[m"
      f"\n\033[1:38mTANGENTE: {tan(radians(a)):.2f}\033[m")
