lista = [1, 9 , 15, 25, -5, 14, 22]

def ordenar_lista(lista):
    """Ordenação de uma lista"""
    lista_ordenada = sorted(lista)
    return lista_ordenada

print(f"Lista original: {lista}")
print(f"lista ordenada: {ordenar_lista(lista)}")