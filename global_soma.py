valor_um = 10
valor_dois = 5
resultado = 0

def somar():
    global resultado
    resultado = valor_um + valor_dois


print("Valor antes da soma")
print(f"Valor 1 = {valor_um}")
print(f"Valor 2 = {valor_dois}")
print(f"Resultado = {resultado}")

print("Valor depois da soma")
somar()
print(f"Valor 1 = {valor_um}")
print(f"Valor 2 = {valor_dois}")
print(f"Resultado = {resultado}")