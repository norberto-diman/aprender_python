# 2. Descobrir se a pessoa é maior de idade
# Peça a idade do usuário e mostre:
# “Maior de idade”
# “Menor de idade”

age = int(input("Qual é a sua idade: "))

if age >= 18:
    print(f"Você tem {age}, você é maior de idade.")
else:
    print(f"Você tem {age}, você é menor de idade.")