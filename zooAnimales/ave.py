from zooAnimales.animal import Animal

class Ave(Animal):


    _listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self.setColorPlumas(colorPlumas)
        Ave._listado.append(self)

    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)

    def movimiento(self):
        return "volar"

    @classmethod
    def crearHalcon(cls, nombre_nuevo, edad_nueva, genero_nuevo):
        halcon = Ave(nombre_nuevo, edad_nueva, "montanas", genero_nuevo, "cafe glorioso")
        cls.halcones += 1
        return halcon

    @classmethod
    def crearAguila(cls, nombre_nuevo, edad_nueva, genero_nuevo):
        aguila = Ave(nombre_nuevo, edad_nueva, "montanas", genero_nuevo, "blanco y amarillo")
        cls.aguilas += 1
        return aguila

    def getColorPlumas(self):
        return self._colorPlumas

    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas

    @classmethod
    def getListado(cls):
        return cls._listado

    @classmethod
    def setListado(cls, listado):
        cls._listado = listado