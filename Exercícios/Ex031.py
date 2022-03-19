from emoji import emojize

print("-" * 39, emojize("\n "
                        "\033[34m:car:  :car:  :car:\033[m "
                        "\033[4:36mAGÊNCIA DE LOCAÇÃO\033[m "
                        "\033[34m:car:  :car:  :car:\033[m \n",
                        use_aliases=True) + "-" * 39, )
d = float(input("Digite a distância da viagem (km): "))
# if d > 200:
#    print(emojize(f"O preço cobrado será de {0.45 * d:.2f} R$ :moneybag::moneybag:",
#                  use_aliases=True))
# else:
#    print(emojize(f"O preço cobrado será de {0.50 * d:.2f} R$ :moneybag: :moneybag:", use_aliases=True))
print(emojize(f"O preço cobrado será de {0.45 * d:.2f} R$ \033[33m:moneybag: :moneybag:\033[m" if d > 200
              else f"O preço cobrado será de {0.50 * d:.2f} R$ \033[33m:moneybag: :moneybag:\033[m",
              use_aliases=True))
print(emojize(":car: "*15, use_aliases=True))
