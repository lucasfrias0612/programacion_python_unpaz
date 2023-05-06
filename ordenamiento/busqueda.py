def busqueda_secuencial(medicamentos, to_search):
    pos = 0
    encontrado = False
    while pos < len(medicamentos) and not encontrado:
        if medicamentos[pos].get_troquel() == to_search:
            encontrado = True
        else:
            pos = pos + 1
    if encontrado:
        return pos
    else:
        return -1


def busqueda_binaria(lista, x):
    """
    Precondición: lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    """
    izq = 0  # izq guarda el índice inicio del segmento
    der = len(lista) - 1  # der guarda el índice fin del segmento
    # un segmento es vacío cuando izq > der:
    while izq <= der:
        medio = round((izq + der) / 2)  # el punto medio del segmento
        # print(f"lista[medio]: {lista[medio].get_troquel()} == x: {x} : {lista[medio].get_troquel() == x}")
        if lista[medio].get_troquel() == x:  # si el medio es igual al valor buscado, lo devuelve
            return medio
        elif lista[medio].get_troquel() > x:
            der = medio - 1
        else:
            izq = medio + 1
    return -1
