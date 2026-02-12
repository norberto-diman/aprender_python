def calcular_fatorial(n):
    if n <= 1:
        return 1
    return n * calcular_fatorial(n - 1)


print(calcular_fatorial(5))
