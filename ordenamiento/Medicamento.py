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
