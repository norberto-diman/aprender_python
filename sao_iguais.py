# 3. Verificar se dois números são iguais
# Receba dois números e diga:
# “São iguais”
# “São diferentes”

number_one = int(input("Digite um número: "))
number_two = int(input("Digite mais um número: "))

if number_one == number_two:
    print(f"{number_one} = {number_two}")
else:
    print(f"{number_one} != {number_two}")