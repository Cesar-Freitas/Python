print("="*5, "NÚMEROS", "="*5, '\nEntre 1 e 50 temos\nos seguintes\nnúmeros pares:')

'''for c in range(1, 51):  # outra sintaxe possível, demanda mais processamento
    if c % 2 == 0:
        print(c)'''

for c in range(2, 51, 2):
    print(c)
