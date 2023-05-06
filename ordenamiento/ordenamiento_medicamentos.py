from datetime import datetime
def datetime_to_locale_string(datetime):
    return f"{datetime.day}/{datetime.month}/{datetime.year} {datetime.hour}:{datetime.minute}:{datetime.second}"

def burbuja(medicamentos):
    startime = datetime.now()
    n = len(medicamentos)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if medicamentos[j].get_troquel() > medicamentos[j + 1].get_troquel():
                aux = medicamentos[j]
                medicamentos[j] = medicamentos[j + 1]
                medicamentos[j + 1] = aux
    endtime = datetime.now()
    return (endtime - startime).total_seconds()

def seleccion(arreglo):
    startime = datetime.now()
    longitud = len(arreglo)
    for i in range(longitud - 1):
        min_idx = i
        for j in range(i + 1, longitud):
            if arreglo[min_idx].get_troquel() > arreglo[j].get_troquel():
                min_idx = j
        # Swapping
        if i != min_idx:
            aux = arreglo[i]
            arreglo[i] = arreglo[min_idx]
            arreglo[min_idx] = aux
    endtime = datetime.now()
    return (endtime - startime).total_seconds()


def merge_sort(medicamentos, lista_temporaria, inicio, fin):
    startime = datetime.now()
    if inicio < fin:
        medio = (inicio + fin) // 2
        merge_sort(medicamentos, lista_temporaria, inicio, medio)
        merge_sort(medicamentos, lista_temporaria, medio + 1, fin)
        merge(medicamentos, lista_temporaria, inicio, medio + 1, fin)
    endtime = datetime.now()
    return (endtime - startime).total_seconds()


def merge(medicamentos, lista_temporaria, inicio, medio, fin):
    fin_primera_parte = medio - 1
    indice_temporario = inicio
    tamano_de_lista = fin - inicio + 1
    while inicio <= fin_primera_parte and medio <= fin:
        if medicamentos[inicio].get_troquel() <= medicamentos[medio].get_troquel():
            lista_temporaria[indice_temporario] = medicamentos[inicio]
            inicio += 1
        else:
            lista_temporaria[indice_temporario] = medicamentos[medio]
            medio += 1
        indice_temporario += 1
    while inicio <= fin_primera_parte:
        lista_temporaria[indice_temporario] = medicamentos[inicio]
        indice_temporario += 1
        inicio += 1
    while medio <= fin:
        lista_temporaria[indice_temporario] = medicamentos[medio]
        indice_temporario += 1
        medio += 1
    for i in range(0, tamano_de_lista):
        medicamentos[fin] = lista_temporaria[fin]
        fin -= 1


def quick_sort(medicamentos, inicio, fin):
    startime = datetime.now()
    if inicio > fin:
        return
    anterior = inicio
    posterior = fin
    pivot = medicamentos[inicio]
    while anterior < posterior:
        while anterior < posterior and medicamentos[posterior].get_troquel() > pivot.get_troquel():
            posterior = posterior - 1
        if anterior < posterior:
            medicamentos[anterior] = medicamentos[posterior]
            anterior = anterior + 1
        while anterior < posterior and medicamentos[anterior].get_troquel() <= pivot.get_troquel():
            anterior = anterior + 1
        if anterior < posterior:
            medicamentos[posterior] = medicamentos[anterior]
            posterior = posterior - 1
        medicamentos[anterior] = pivot
    quick_sort(medicamentos, inicio, anterior - 1)
    quick_sort(medicamentos, anterior + 1, fin)
    endtime = datetime.now()
    return (endtime - startime).total_seconds()
