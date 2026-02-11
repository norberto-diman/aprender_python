# 3️⃣ Somar apenas números pares
# Crie uma lista de números. Use for e if/else para somar somente os números pares da lista.

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = len(lista_numeros)
soma = 0
for i in range (numeros):
    if lista_numeros[i] % 2 == 0:
        soma = soma + lista_numeros[i]

print(f'A soma dos números pares é de {soma}')
