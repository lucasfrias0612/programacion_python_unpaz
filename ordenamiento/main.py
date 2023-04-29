from CSVService import CSVService
from datetime import datetime

class Medicamento:
    def __init__(self, troquel, nombre_comercial, presentacion, laboratorio, pvp, psl):
        self.__troquel = int(troquel)
        self.__nombre_comercial = nombre_comercial
        self.__presentacion = presentacion
        self.__laboratorio = laboratorio
        self.__pvp = float(pvp)
        self.__psl = float(psl)

    def get_troquel(self):
        return self.__troquel

    def get_nombre_comercial(self):
        return self.__nombre_comercial

    def get_presentacion(self):
        return self.__presentacion

    def get_laboratorio(self):
        return self.__laboratorio

    def get_pvp(self):
        return self.__pvp

    def get_psl(self):
        return self.__psl

    def __str__(self):
        return f"Troquel: {self.__troquel} - Nombre comercial: {self.__nombre_comercial} - Presentación: {self.__presentacion} - Laboratorio: {self.__laboratorio} - PVP: {self.__pvp} - PSL: {self.__psl} "


def seleccion(arreglo):
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


def burbuja(medicamentos):
    n = len(medicamentos)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if medicamentos[j].get_troquel() > medicamentos[j + 1].get_troquel():
                aux = medicamentos[j]
                medicamentos[j] = medicamentos[j + 1]
                medicamentos[j + 1] = aux


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
        #print(f"lista[medio]: {lista[medio].get_troquel()} == x: {x} : {lista[medio].get_troquel() == x}")
        if lista[medio].get_troquel() == x:  # si el medio es igual al valor buscado, lo devuelve
            return medio
        elif lista[medio].get_troquel() > x:
            der = medio - 1
        else:
            izq = medio + 1
    return -1

def datetime_to_locale_string(datetime):
    return f"{datetime.day}/{datetime.month}/{datetime.year} {datetime.hour}:{datetime.minute}:{datetime.second}"

def print_list(p_list, list_name):
    print(f"\nListando {list_name}")
    for element in p_list:
        print(element)

CSV_SERVICE = CSVService('medicamentos.csv')
MEDICAMENTOS = []
for row in CSV_SERVICE.get_data():
    MEDICAMENTOS.append(Medicamento(row[0], row[1], row[2], row[3], row[4], row[5]))

top_100_medicamentos = MEDICAMENTOS[0:99]
top_1000_medicamentos = MEDICAMENTOS[0:999]
top_10000_medicamentos = MEDICAMENTOS[0:9999]

#Cambiar cantidad de registros a procesar con ambos algoritmos
MEDICAMENTOS=top_1000_medicamentos
copia_todos_los_medicamentos = MEDICAMENTOS[0:len(MEDICAMENTOS) - 1]

"""
print(f"Ordenando top 10000 medicamentos ({len(top_10000_medicamentos)})")
seleccion(top_10000_medicamentos)
print("Todos los medicamentos ordenados")
"""

print_list(MEDICAMENTOS, "MEDICAMENTOS")
seleccion_startime=datetime.now()
print(f"Ordenando medicamentos por seleccion... start {datetime_to_locale_string(seleccion_startime)}")
seleccion(MEDICAMENTOS)
seleccion_endtime=datetime.now()
print(f"Medicamentos ordenados por seleccion %.2f segundos"%(seleccion_endtime-seleccion_startime).total_seconds())
print_list(MEDICAMENTOS, "MEDICAMENTOS")

burbuja_startime=datetime.now()
print_list(copia_todos_los_medicamentos, "copia_todos_los_medicamentos")
print(f"Ordenando medicamentos por burbuja... start {datetime_to_locale_string(burbuja_startime                 )}")
burbuja(copia_todos_los_medicamentos)
burbuja_endtime=datetime.now()
print(f"Medicamentos ordenados por burbuja %.2f segundos"%(burbuja_endtime-burbuja_startime).total_seconds())
print_list(copia_todos_los_medicamentos, "copia_todos_los_medicamentos")

entrada=""
while entrada != 0:
    entrada = int(input("Ingrese troquel a buscar: "))
    resultado=busqueda_binaria(MEDICAMENTOS,entrada)
    if resultado!=-1:
        print(f"El medicamento es {MEDICAMENTOS[resultado]}")
    else:
        print(f"No se econtró el medicamento con troquel {entrada}")