# print("\033[1:35:40mOlá mundo\033[m")
a = 1
b = 3
nomes = ['Ricardo', 'Paulo', 'João', 'Carmem']
# print(f"Os valores são \033[31m{a}\033[m e \033[36m{b}\033[m!!") !!ERRADO
# print(f"Os valores são {'\033[4;34m'}{a}{'\033[m'} e {'\033[4:30'}{b}{'\033[m'}") !!ERRADO
# print("Seja bem vindo {}{}{}".format('\033[4:30m', n, '\033[m'))
cores = {'azul': '\033[4:34m',
         'vermelho': '\033[4:31',
         'verde': '\033[4:32m',
         'limpa': '\033[m'}
print("Seja bem vindo {}{}{}".format(cores['azul'], nomes[3], cores['limpa']))
