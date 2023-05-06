from datetime import datetime


def datetime_to_locale_string(datetime):
    return f"{datetime.day}/{datetime.month}/{datetime.year} {datetime.hour}:{datetime.minute}:{datetime.second}"


def burbuja(alumnos):
    startime = datetime.now()
    n = len(alumnos)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if alumnos[j].get_promedio() > alumnos[j + 1].get_promedio():
                aux = alumnos[j]
                alumnos[j] = alumnos[j + 1]
                alumnos[j + 1] = aux
    endtime = datetime.now()
    return (endtime - startime).total_seconds()


def seleccion(alumnos):
    startime = datetime.now()
    longitud = len(alumnos)
    for i in range(longitud - 1):
        min_idx = i
        for j in range(i + 1, longitud):
            if alumnos[min_idx].get_promedio() > alumnos[j].get_promedio():
                min_idx = j
        # Swapping
        if i != min_idx:
            aux = alumnos[i]
            alumnos[i] = alumnos[min_idx]
            alumnos[min_idx] = aux
    endtime = datetime.now()
    return (endtime - startime).total_seconds()


def merge_sort(alumnos, lista_temporaria, inicio, fin):
    startime = datetime.now()
    if inicio < fin:
        medio = (inicio + fin) // 2
        merge_sort(alumnos, lista_temporaria, inicio, medio)
        merge_sort(alumnos, lista_temporaria, medio + 1, fin)
        merge(alumnos, lista_temporaria, inicio, medio + 1, fin)
    endtime = datetime.now()
    return (endtime - startime).total_seconds()


def merge(alumnos, lista_temporaria, inicio, medio, fin):
    fin_primera_parte = medio - 1
    indice_temporario = inicio
    tamano_de_lista = fin - inicio + 1
    while inicio <= fin_primera_parte and medio <= fin:
        if alumnos[inicio].get_promedio() <= alumnos[medio].get_promedio():
            lista_temporaria[indice_temporario] = alumnos[inicio]
            inicio += 1
        else:
            lista_temporaria[indice_temporario] = alumnos[medio]
            medio += 1
        indice_temporario += 1
    while inicio <= fin_primera_parte:
        lista_temporaria[indice_temporario] = alumnos[inicio]
        indice_temporario += 1
        inicio += 1
    while medio <= fin:
        lista_temporaria[indice_temporario] = alumnos[medio]
        indice_temporario += 1
        medio += 1
    for i in range(0, tamano_de_lista):
        alumnos[fin] = lista_temporaria[fin]
        fin -= 1


def quick_sort(alumnos, inicio, fin):
    startime = datetime.now()
    if inicio > fin:
        return
    anterior = inicio
    posterior = fin
    pivot = alumnos[inicio]
    while anterior < posterior:
        while anterior < posterior and alumnos[posterior].get_promedio() > pivot.get_promedio():
            posterior = posterior - 1
        if anterior < posterior:
            alumnos[anterior] = alumnos[posterior]
            anterior = anterior + 1
        while anterior < posterior and alumnos[anterior].get_promedio() <= pivot.get_promedio():
            anterior = anterior + 1
        if anterior < posterior:
            alumnos[posterior] = alumnos[anterior]
            posterior = posterior - 1
        alumnos[anterior] = pivot
    quick_sort(alumnos, inicio, anterior - 1)
    quick_sort(alumnos, anterior + 1, fin)
    endtime = datetime.now()
    return (endtime - startime).total_seconds()
