def quadrado(value):
    if eh_par(value):
        return value ** 2
    else:
        return value / 2

def eh_par(value):
    if value % 2 == 0:
        return True
    else:
        return False


print(quadrado(3))