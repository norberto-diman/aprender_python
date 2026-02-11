# 4. Identificar o maior número entre dois
# Receba dois números e mostre qual deles é maior.
# (Fluxograma clássico de decisão)

number_one = int(input("Digite um número: "))
number_two = int(input("Digite mais um número: "))

if number_one > number_two:
    print(f"{number_one} > {number_two}")
else: 
    print(f"{number_one} < {number_two}")