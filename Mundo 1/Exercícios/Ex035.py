from emoji import emojize
print("-"*43)
a = float(input("\033[32mDigite o comprimento do primeiro lado: \033[m"))
b = float(input("\033[33mDigite o comprimento do segundo lado: \033[m"))
c = float(input("\033[34mDigite o comprimento do terceiro lado: \033[m"))
print("-"*43)
if a < b + c and b < a + c and c < a + b:
    print(emojize("\033[35mOs lados formam um triângulo! :triangular_ruler:\033[m", use_aliases=True))
else:
    print(emojize("\033[31mOs lados não formam um triângulo! :x:\033[m", use_aliases=True))
'''
d = b - c
if d < 0:
    d = d * (-1)
if b - c < a < b + c:
    print(emojize("Os lados formam um triângulo :triangular_ruler:", use_aliases=True))
else:
    print(emojize("Os lados não formam um triângulo! :x:", use_aliases=True))
'''