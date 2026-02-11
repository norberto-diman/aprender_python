# 9️⃣ Contar vogais e consoantes
# Dada uma lista de letras, percorra-a e conte:
# quantas são vogais
# quantas são consoantes


lista_letras = ['a', 'b', 'c', 'd', 'e', 'f']
letras = len(lista_letras)
contador = [0, 0]

for i in range (letras):
    if lista_letras[i] in ('a', 'e', 'i', 'o', 'u'):
        contador[0] = contador[0] + 1
    else:
        contador[1] = contador[1] + 1

print(f'Número de vogais é {contador[0]} | Número de consoantes é {contador[1]}')
