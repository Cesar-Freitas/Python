# v = float(input("Digite a velocidade do carro: "))
# if v > 80.00:
#    print(f"Você ultrapassou o limite de velocidade e precisará pagar uma multa de "
#          f"{(v - 80.00)*7:.2f} R$")
# else:
#    print("Sua velocidade está dentro do limite!")
# ----------------------------------------------------------------------------------------
import emoji
print("-" * 35, emoji.emojize("\n    :busstop:  :busstop:  :busstop: \033[4:35m RADAR \033[m "
                              ":busstop:  :busstop:  :busstop:\n", use_aliases=True) + "-"*35)
v = float(input(emoji.emojize(":traffic_light: INFORME A VELOCIDADE DO CARRO: ", use_aliases=True)))
print(emoji.emojize(f"Você ultrapassou o limite de velocidade \033[1:31m :warning: \033[m \nTerá que pagar uma multa de "
                    f"R$ {(v - 80.00)*7:.2f} \033[1:33m :money_with_wings: :money_with_wings: \033[m" if v > 80.00
      else "Você está dentro do limite de velocidade \033[1:32m :white_check_mark: \033[m", use_aliases=True))
print("-"*35, emoji.emojize("\n          :red_car:                 :police_car: ", use_aliases=True))
# Se precisamos de apenas uma condição, não é necessário colocar o 'else', podemos apenas
# escrever como uma linha qualquer
