from emoji import emojize
print("* "*6 + "IMC", "* "*6)
m = float(input("DIGITE SUA MASSA (kg): "))
h = float(input("DIGITE SUA ALTURA (m): "))
imc = m / h ** 2
print("- "*14, "\nSeu IMC é de {:.2f} e ".format(imc), end="")
if imc < 18.5:
    # abaixo do peso - cinza
    print("você está \033[37mABAIXO DO PESO\033[m, precisa se alimentar mais!")
elif imc <= 25:
    # peso ideal - branco
    print("você está no \033[30mPESO IDEAL\033[m, parabéns!")
elif imc <= 30:
    # sobrepeso - amarelo
    print("você está no \033[33mSOBREPESO\033[m, vamos aumentar o cuidado com a saúde!")
elif imc <= 40:
    # obesidade - verde
    print("você está na \033[32mOBESIDADE\033[m, precisa tomar cuidado!")
else:
    # obesidade mórbida - vermelho
    print(emojize("você está na :warning: \033[31mOBESIDADE MÓRBIDA\033[m :warning:, "
                  "precisa consultar um médico imediatamente!", use_aliases=True))
