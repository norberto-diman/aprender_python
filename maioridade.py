# 🔟 Verificar maioridade
# Dada uma lista de idades, percorra a lista e imprima:
# “Maior de idade” se idade ≥ 18
# “Menor de idade” caso contrário

lista_idades = [29, 17, 21, 40, 90, 200, 18, 16]
idades = len(lista_idades)

for i in range (idades):
    if lista_idades[i] >= 18:
        print(f'Você tem {lista_idades[i]}, portanto é mair de idade!')
    else:
        print(f'Você tem {lista_idades[i]}, portanto é menor de idade!')