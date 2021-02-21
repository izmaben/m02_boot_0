class Perro():
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        
    def ladrar(self):
        if self.peso >=8:
            print("GUAU, GUAU")
        else:
            print("ay, ay")
            
    def __str__(self):
        return "Perro {}, e: {}, p: {}".format(self.nombre, self.edad, self.peso)
    
class PerroAsistencia(Perro):
    trabajando = False
    
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo
        
    def __str__(self):
        return "Perro de asistencia de {}".forma(self.amo)
    
    def pasear(self):   
        return print("{} ayudo a mi dueña, {} a pasear".format(self.nombre, self.amo))
    
    def ladrar(self):
        if self.__trabjando:
            print("shhhh, no puedo ladrar")
        else:
            Perro.ladrar(self)
            
    def trabajando(self, valor=None):
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor
            
    