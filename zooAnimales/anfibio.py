from zooAnimales.animal import Animal


class Anfibio(Animal):

    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self.setColorPiel(colorPiel)
        self.setVenenoso(venenoso)
        Anfibio._listado.append(self)

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)

    def movimiento(self):
        return "saltar"

    @classmethod
    def crearRana(cls, nombre_nuevo, edad_nueva, genero_nuevo):
        rana = Anfibio(nombre_nuevo, edad_nueva, "selva", genero_nuevo, "rojo", True)
        cls.ranas += 1
        return rana

    @classmethod
    def crearSalamandra(cls, nombre_nuevo, edad_nueva, genero_nuevo):
        salamandra = Anfibio(nombre_nuevo, edad_nueva, "selva", genero_nuevo, "negro y amarillo", False)
        cls.salamandras += 1
        return salamandra

    def getColorPiel(self):
        return self._colorPiel

    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel

    def isVenenoso(self):
        return self._venenoso

    def setVenenoso(self, venenoso):
        self._venenoso = venenoso

    @classmethod
    def getListado(cls):
        return cls._listado

    @classmethod
    def setListado(cls, listado):
        cls._listado = listado
