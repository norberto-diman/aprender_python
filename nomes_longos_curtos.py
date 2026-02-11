# 7️⃣ Nomes longos e curtos
# Dada uma lista de nomes, imprima:
# “Nome longo” se tiver mais de 5 letras
# “Nome curto” caso contrário

lista_nomes = ['José', 'Josefa', 'Antonio', 'Aparecida', 'Jade']
nomes = len(lista_nomes)

for i in range (nomes):

    if len(lista_nomes[i]) > 5:
        print(f'O nome {lista_nomes[i]} é um nome longo!')
    else:
        print(f'O nome {lista_nomes[i]} é um nome curto!')