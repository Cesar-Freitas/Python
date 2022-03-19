n = input("Digite algo: ")
t = type(n)
sp = n.isspace()
num = n.isnumeric()
alf = n.isalpha()
aln = n.isalnum()
mai = n.isupper()
mn = n.islower()
cap = n.istitle()
print(f"O tipo primitivo do que foi digitado: {t}"
      f"\nSó tem espaços? {sp}\nÉ um número? {num}\nÉ alfabético? {alf}\nÉ alfanumérico? {aln}\n"
      f"Está em maiúsculo? {mai}\nEstá em minúsculo? {mn}\nEstá capitalizado? {cap}")
