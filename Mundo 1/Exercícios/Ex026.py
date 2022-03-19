f = input("Digite uma frase: ")
# ou f = input("Digite uma frase: ").strip().upper()

print(f"A letra 'A' aparece \033[1:32m{f.upper().strip().count('A')}\033[m vezes, "
      f"na \033[1:35m{f.upper().strip().find('A') + 1}ª\033[m posição pela primeira vez e na "
      f"\033[1:38m{f.upper().strip().rfind('A') + 1}ª\033[m uma última vez.")
