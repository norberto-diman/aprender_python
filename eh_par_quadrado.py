def calcular_quadrado(value):
    if verificar_eh_par(value):
        return value ** 2
    else:
        return value / 2

def verificar_eh_par(value):
    if value % 2 == 0:
        return True
    else:
        return False


print(calcular_quadrado(3))