from emoji import emojize
print('-'*37)
a = float(input("\033[35mDIGITE O VALOR DO PRIMEIRO LADO\033[m: "))
b = float(input("\033[36mDIGITE O VALOR DO SEGUNDO LADO\033[m: "))
c = float(input("\033[34mDIGITE O VALOR DO TERCEIRO LADO\033[m: "))
print('-'*37)
# Sistema para saber se tem triângulo ou não
if a < b + c and b < a + c and c < a + b:
    print(emojize("\033[32mAs medidas formam um triângulo\033[m "
                  ":triangular_ruler: :heavy_check_mark:", use_aliases=True))
    if a == b == c:
        print("O triângulo formado é do tipo EQUILÁTERO!!")
    elif a == b or a == c or b == c:
        print("O triângulo formado é do tipo ISÓCELES!!")
    else:
        print("O triângulo formado é do tipo ESCALENO!!")
else:
    print(emojize("\033[31mAs medidas não formam um triângulo :x:", use_aliases=True))
