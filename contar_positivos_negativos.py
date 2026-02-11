# 2️⃣ Contar números positivos e negativos
# Dada uma lista de números, percorra-a e conte quantos são positivos e quantos são negativos.

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5]
numeros = len(lista_numeros)
contador = [0, 0]

for i in range (numeros):
    if lista_numeros[i] > 0:
        contador[0] = contador[0] + 1
    else:
        contador[1] = contador[1] + 1

print(f'{contador[0]} são positivos!')
print(f'{contador[1]} são negativos!')