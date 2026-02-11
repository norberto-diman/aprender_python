# 1️⃣ Verificar números pares e ímpares
# Crie uma lista de números inteiros. Percorra a lista com for e, usando if/else, imprima se cada número é par ou ímpar.


lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = len(lista_numeros)
for i in range (numeros):
    if lista_numeros[i] % 2 == 0:
        print(f'{lista_numeros[i]} é par!')
    else:
        print(f'{lista_numeros[i]} é impar!')
