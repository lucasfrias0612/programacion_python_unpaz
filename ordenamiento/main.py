from CSVService import CSVService
from datetime import datetime
from ordenamiento_alumnos import burbuja, seleccion, merge_sort, quick_sort
from busqueda import busqueda_secuencial, busqueda_binaria
from Medicamento import Medicamento
from Alumno import Alumno


def print_list(p_list, list_name):
    print(f"\nListando {list_name}")
    for element in p_list:
        print(element)


def ordenar(lista, metodo):
    metodo = metodo.lower()
    tamano_de_lista = len(lista)
    if tamano_de_lista > 0:
        if metodo == 'quicksort':
            quick_sort(lista, 0, tamano_de_lista - 1)
        elif metodo == 'mergesort':
            lista_temporaria = [0] * tamano_de_lista
            merge_sort(lista, lista_temporaria, 0, tamano_de_lista - 1)
        elif metodo == 'burbuja':
            burbuja(lista)
        elif metodo == 'seleccion':
            seleccion(lista)
        else:
            raise ValueError("El parametro método debe ser 'quicksort' o 'mergesort'")
    else:
        raise ValueError("No se puede ordenar una lista vacía")


ALUMNOS = [Alumno(1, 'pepe', 7.5), Alumno(2, 'carlos', 6.5), Alumno(3, 'jose', 5), Alumno(4, 'pamela', 8),
           Alumno(5, 'Pablo', 5), Alumno(6, 'jesica', 9), Alumno(7, 'Vilma', 3), Alumno(8, 'alberto', 10),
           Alumno(9, 'Carla', 4), Alumno(10, 'Maria', 9)]

sumatoria=0
for alumno in ALUMNOS:
    sumatoria+=alumno.get_promedio()
    print(alumno)
promedio_gral=sumatoria/len(ALUMNOS)
burbuja(ALUMNOS)
print('Promedio general: %.2f'%promedio_gral)


for i in range(len(ALUMNOS)-1,0,-1):
    if ALUMNOS[i].get_promedio() >= promedio_gral:
        print(ALUMNOS[i])

