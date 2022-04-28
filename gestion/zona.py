class Zona():
    def __init__(self, nombre = None , zoo = None):
        self.setNombre(nombre)
        self.setZoo(zoo)
        self._animales = []

    def agregarAnimales(self, animal):
        self.getAnimales().append(animal)
        animal.setZona(self)

    def cantidadAnimales(self):
        return len(self.getAnimales())

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getZoo(self):
        return self._zoo

    def setZoo(self, zoo):
        self._zoo = zoo

    def getAnimales(self):
        return self._animales

    def setAnimales(self, animales):
        _animales = animales