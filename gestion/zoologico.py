class Zoologico():

    _zonas = []
    def __init__(self, nombre = None, ubicacion = None):
        self.setNombre(nombre)
        self.setUbicacion(ubicacion)

    def agregarZonas(self, zona):
        self.getZona().append(zona)

    def cantidadTotalAnimales(self):
        numAnimales = 0
        for i in range (len(self.getZona())):
            zonaActual = self.getZona()[i]
            animales = zonaActual.getAnimales()
            numAnimales += len(animales)
        return numAnimales

    def getNombre(self):
        return self._nombre


    def setNombre(self, nombre):
        self._nombre = nombre


    def getUbicacion(self):
        return self._ubicacion


    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion


    def getZona(self):
        return Zoologico._zonas


    def setZonas(self, zonas):
        Zoologico._zonas = zonas