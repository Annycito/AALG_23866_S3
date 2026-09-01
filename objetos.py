# perro p= new Perro
#perro q= new Perro ("fido", 5);
class Perro:
    def __init__(self , nombre="", edad=0   ):
        self.nombre = nombre
        self.edad = edad
    def ladrar(self):
        return f"{self.nombre} dice: Guau Guau"
    def __str__(self):
        return f"Nombre: {self.nombre}, tienes: {self.edad} años"

P=Perro()
q=Perro("Fido", 5)
print(q.ladrar())
print(q)
