# 1. Verificar se um número é positivo ou negativo
# Peça ao usuário um número e exiba:
# “Positivo” se for maior que zero
# “Negativo” se for menor que zero
# “Zero” caso contrário


number = int(input("Digite um número: "))

if number > 0:
    print(f"O número {number} é positivo.")
elif number < 0:
    print(f"O número {number} é negativo.")
else:
    print(f"O número é {number}.")