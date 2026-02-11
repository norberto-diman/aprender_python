# 5️⃣ Verificar aprovação dos alunos
# Dada uma lista de notas, percorra a lista e, para cada nota:
# imprima “Aprovado” se a nota for ≥ 7
# “Reprovado” caso contrário

lista_notas = [8.5, 6.0, 7.2, 4.5, 9.0, 5.5]
notas = len(lista_notas)
for i in range (notas):
    if lista_notas[i] >= 7:
        print(f'Sua nota é {lista_notas[i]}, você está Aprovado!')
    else:
        print(f'Sua nota é {lista_notas[i]}, você está Reprovado!') 