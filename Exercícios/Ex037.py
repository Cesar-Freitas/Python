from emoji import emojize
n = int(input("Digite um número: "))
# print('''Escolha a base numérica para a qual o número será convertido:"
#      [1] BINÁRIO
#      [2] OCTAL
#      [3] HEXADECIMAL''')
print("Escolha a base para a qual o número será convertido:\n[1] BINÁRIO\n[2] OCTAL\n[3] HEXADECIMAL")
s = int(input("OPÇÃO: "))
if s == 1:
    # print(bin(n)[2:])
    print(format(n, 'b'))
elif s == 2:
    # print(oct(n)[2:])
    print(format(n, 'o'))
elif s == 3:
    # print(hex(n)[2:])
    # print(format(n, 'X')) --> as letras saem em maiúsculo
    print(format(n, 'x'))
else:
    print(emojize("\033[31m:x: OPÇÃO INVÁLIDA", use_aliases=True))
