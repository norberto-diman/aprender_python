# 4️⃣ Substituir valores negativos
# Dada uma lista de números, percorra-a e crie uma nova lista onde:
# números negativos viram 0
# números positivos permanecem iguais

lista_numeros = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
numeros = len(lista_numeros)
lista_numeros_dois = []

for i in range(numeros):
    if lista_numeros[i] < 0:
        lista_numeros_dois.append(0)
    else:
        lista_numeros_dois.append(lista_numeros[i])

print(lista_numeros)
print(lista_numeros_dois)