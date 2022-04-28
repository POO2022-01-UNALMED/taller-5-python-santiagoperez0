class Animal():


    _totalAnimales = 0
    def __init__(self, nombre = None, edad  = 0, habitat = None, genero = None):
        self.setNombre(nombre)
        self.setEdad(edad)
        self.setHabitat(habitat)
        self.setGenero(genero)
        self._zona = None
        Animal._totalAnimales += 1

    def movimiento(self):
        return "desplazarse"


    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.ave import Ave
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        cadena = 'Mamiferos : ' + str(Mamifero.cantidadMamiferos())+ '\nAves : ' + str(Ave.cantidadAves()) + '\nReptiles : ' + str(Reptil.cantidadReptiles()) + '\nPeces : ' + str(Pez.cantidadpeces()) + '\nAnfibios : ' + str(Anfibio.cantidadAnfibios())
        return cadena

    def toString(self):
        if self.getZona() is not None:
            return "Mi nombre es" + self.getNombre() + ", tengo una edad de " + str(self.getEdad()) + ", habito en " + self.getHabitat() + " y mi genero es " + self.getGenero() + ", la zona en la que me ubico es " + self._zona + ", en el " + self._zona.getZoo()
        else:
            return "Mi nombre es " + self.getNombre() + ", tengo una edad de " + str(self.getEdad()) + ", habito en " + self.getHabitat() + " y mi genero es " + self.getGenero()


    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat

    def setHabitat(self, habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero

    def getZona(self):
        return self._zona

    def setZona(self, zona):
        self._zona = zona