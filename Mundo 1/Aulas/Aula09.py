frase = "   Amo Física, é a mãe de todas as ciências  asd "
# atribuição duma string à uma variável
# print(frase[2])
# print(frase[0:4])  # vai do caractere 0 ao 4, excluindo o 4
# print(frase[0:10])
# print(frase[0:15:2])  # vai do crc.0 ao crc.15 saltando de 2 em 2
# print(frase[:13])  # começa do caractere inicial e termina ele no caractere 13
# print(frase[13:0:-2])  # vai do crc.13 até o final, o -2 faz ele inverter
# print(frase[2::10])  # começa do crc.2 e vai até o final saltando de 10 em 10
# --------------------------------------------------------------------------------------------
# print(len(frase))
# print(frase.count('i', 0, 10))  # Busca de caracteres até o caractere 10
# print(frase.find('mãe'))  # Em que posição COMEÇA a string 'mãe'
# print(frase.find("banana"))  # -1 indica que essa string não existe
# --------------------------------------------------------------------------------------------
# print("Física" in frase)  # Operador lógico para identificar se há ou não essa string
# print(frase.replace("Física", "Matemática"))
# print(frase.upper())
# print(frase.lower())
# print(frase.capitalize())  # Deixa apenas o primeiro crc. em maiúsculo e passa o restante para minúsculo
# print(frase.title())  # Coloca tudo o que vem em seguida do espaço em maiúsculo
# print(frase.strip())  # Remove todos os espaços desnecessários
# print(frase.rstrip())  # Remove todos os espaços desnecessários à direita. A mesma lógica para lstrip
# --------------------------------------------------------------------------------------------
# print(frase.split())  # Gera uma lista, dividindo uma string pelo espaço. Ao colocar
#                                algo dentro do (), definimos nosso separador
# print(frase.split()[1])
# print(frase.split()[1][3])  # Mostra o crc. de nº 3 no primeiro elemento da lista
# print("=".join(frase))  # Cerca cada crc. com um tracinho
