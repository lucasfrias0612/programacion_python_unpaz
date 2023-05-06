class Alumno:
    def __init__(self, legajo, nombre_y_apellido, promedio_notas):
        self.__legajo=legajo
        self.__nombre_y_apellido=nombre_y_apellido
        self.__promedio_notas=promedio_notas

    def get_promedio(self):
        return self.__promedio_notas

    def __str__(self):
        return f"Legajo: {self.__legajo} - Nombre y apellido: {self.__nombre_y_apellido} - Promedio: {self.__promedio_notas}"
