n = input("Digite o primeiro nome de uma pessoa: ").strip()
print(f"O nome {n.upper()} começa com \033[46:32m'SANTO'\033[m? \n{'SANTO' in n.upper().split()[0]}!")
# == comando lógico de conferência
