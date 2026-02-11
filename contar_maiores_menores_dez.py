# 6️⃣ Contar maiores e menores que 10
# Crie uma lista de números e conte:
# quantos são maiores que 10
# quantos são menores ou iguais a 10

lista_numeros = [4, 15, 8, 23, 42, 7, 10, 3, 12, 9]
numeros = len(lista_numeros)
contador = [0, 0]

for i in range (numeros):
    if lista_numeros[i] > 10:
        contador[0] = contador[0] + 1
    else:
        contador[1] = contador[1] + 1

print(f'{contador[0]} são maiores que 10!')
print(f'{contador[1]} são menores ou iguais a 10!')