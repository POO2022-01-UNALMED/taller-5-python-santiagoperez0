from zooAnimales.animal import Animal


class Reptil(Animal):

    _listado = []
    iguanas = 0
    serpientes = 0
    
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self.setColorEscamas(colorEscamas)
        self.setLargoCola(largoCola)
        Reptil._listado.append(self)

    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)

    def movimiento(self):
        return "reptar"

    @classmethod
    def crearIguana(cls, nombre_nuevo, edad_nueva, genero_nuevo):
        iguana = Reptil(nombre_nuevo, edad_nueva, "humedal", genero_nuevo, "verde", 3)
        cls.iguanas += 1
        return iguana

    @classmethod
    def crearSerpiente(cls, nombre_nuevo, edad_nueva, genero_nuevo):
        serpiente = Reptil(nombre_nuevo, edad_nueva, "jungla", genero_nuevo, "blanco", 1)
        cls.serpientes += 1
        return serpiente

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getLargoCola(self):
        return self._largoCola

    def setLargoCola(self, largoCola):
        self._largoCola = largoCola

    @classmethod
    def getListado(cls):
        return cls._listado

    @classmethod
    def setListado(cls, listado):
        cls._listado = listado