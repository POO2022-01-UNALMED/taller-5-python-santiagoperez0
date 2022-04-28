from zooAnimales.animal import Animal

class Pez(Animal):
    _listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self.setColorEscamas(colorEscamas)
        self.setCantidadAletas(cantidadAletas)
        Pez._listado.append(self)

    @classmethod
    def cantidadpeces(cls):
        return len(cls._listado)

    def movimiento(self):
        return "nadar"

    @classmethod
    def crearSalmon(cls, nombre_nuevo, edad_nueva, genero_nuevo):
        salmon = Pez(nombre_nuevo, edad_nueva, "oceano", genero_nuevo, "rojo", 6)
        cls.salmones += 1
        return salmon

    @classmethod
    def crearBacalao(cls, nombre_nuevo, edad_nueva, genero_nuevo):
        bacalao = Pez(nombre_nuevo, edad_nueva, "oceano", genero_nuevo, "gris", 6)
        cls.bacalaos += 1
        return bacalao

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getCantidadAletas(self):
        return self._cantidadAletas

    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas

    @classmethod
    def getListado(cls):
        return cls._listado

    @classmethod
    def setListado(cls, listado):
        cls._listado = listado