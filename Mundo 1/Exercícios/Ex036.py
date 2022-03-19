# from emoji import emojize
import emoji
import time
# print("=="*8, emoji.emojize(":moneybag: \033[1:31mBANCO SANTO ANDRÉ\033[m3 :moneybag:", use_aliases=True), "=="*8)
print("=="*11, emoji.emojize(":bank: \033[1:31mBANCO SANTO ANDRÉ\033[m :bank:", use_aliases=True), "=="*11)
print("Bem vindos ao sistema de empréstimo. Complete as informações abaixo: ")
v = float(input("Digite o valor da casa: R$ "))
s = float(input("Digite o valor de seu salário: R$ "))
t = int(input("Em quantos anos gostaria de realizar o pagamento: "))
print("CALCULANDO. . .")
time.sleep(3)
p = v/(t*12)
if s*0.3 < p:
    print(emoji.emojize("SITUAÇÃO DO PEDIDO:\033[31m NEGADO :x:", use_aliases=True))
else:
    print(emoji.emojize("SITUAÇÃO DO PEDIDO:\033[32m ACEITO :heavy_check_mark:", use_aliases=True))
