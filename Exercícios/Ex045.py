from random import choice
from emoji import emojize
from time import sleep
n = input("DIGITE O NOME DO PLAYER: ")
pc = int(input(emojize('''ESCOLHA SUA ARMA
--------------------
| [1] -> :fist: 
| [2] -> :wave: 
| [3] -> :v:    
--------------------
OPÇÃO: ''', use_aliases=True)))
if pc != 1 and pc != 2 and pc != 3:
    print("-"*20, emojize("\n" + "\033[31m:x: OPÇÃO INVÁLIDA :x:\033[m", use_aliases=True))
print('-'*20)
sleep(1)
print("JO... ")
sleep(1)
print("..KEN..")
sleep(1)
print("    ..PO")
print('-'*20)
# ----------------------------------------------------------
pedra = emojize(":fist:", use_aliases=True)  # pedra
papel = emojize(":wave:", use_aliases=True)  # papel
tesoura = emojize(":v:", use_aliases=True)   # tesoura
cc = (choice([pedra, papel, tesoura]))
if (pc == 1 and cc == tesoura) or (pc == 2 and cc == pedra) or (pc == 3 and cc == papel):
    if pc == 1:
        pc = emojize(":fist:", use_aliases=True)
    elif pc == 2:
        pc = emojize(":wave:", use_aliases=True)
    elif pc == 3:
        pc = emojize(":v:", use_aliases=True)
    print(emojize("{} ganha de {}. Parabéns pela \033[1:32mVITÓRIA\033[m {} :star2: :star2:"
                  .format(pc, cc, n), use_aliases=True))
elif (pc == 1 and cc == papel) or (pc == 2 and cc == tesoura) or (pc == 3 and cc == pedra):
    if pc == 1:
        pc = emojize(":fist:", use_aliases=True)
    elif pc == 2:
        pc = emojize(":wave:", use_aliases=True)
    elif pc == 3:
        pc = emojize(":v:", use_aliases=True)
    print(emojize("{} perde de {}. Você foi \033[31mDERROTADO(A)\033[m {} :x: :x:".format(pc, cc, n), use_aliases=True))
else:
    if pc == 1:
        pc = emojize(":fist:", use_aliases=True)
    elif pc == 2:
        pc = emojize(":wave:", use_aliases=True)
    elif pc == 3:
        pc = emojize(":v:", use_aliases=True)
    print("{} é igual a {}. O jogo terminou em empate!".format(pc, cc))
