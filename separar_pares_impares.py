# 8️⃣ Separar pares e ímpares
# Crie uma lista de números e, usando for e if/else, coloque:
# os pares em uma lista
# os ímpares em outra

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
numeros = len(lista_numeros)
lista_numeros_pares = []
lista_numeros_impares = []

for i in range (numeros):
    if lista_numeros[i] % 2 == 0:
        lista_numeros_pares.append(lista_numeros[i])
    else:
        lista_numeros_impares.append(lista_numeros[i])


print('Números pares:')
print(lista_numeros_pares)

print('Números Impares:')
print(lista_numeros_impares)