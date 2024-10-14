class CuerpoCeleste:
    def __init__(self, nombre, excentricidad, anomalia_media):
        self.__nombre = nombre
        self.__e = excentricidad
        self.__M = anomalia_media

    @property
    def nombre(self):
        return self.__nombre

    @property
    def e(self):
        return self.__e

    @property
    def M(self):
        return self.__M

    def informacion(self):
        return f"Nombre: {self.__nombre}, Excentricidad: {self.__e}, Anomalía Media: {self.__M}"