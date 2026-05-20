class Perro:
    def __init__(self,nombre,raza,color,edad,peso,tamaño,vacunado,esterelizado,dueño,collar):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad
        self.peso=peso
        self.tamaño=tamaño
        self.vacunado=vacunado
        self.esterelizado=esterelizado
        self.dueño=dueño
        self.collar=collar

        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Color: {self.color}") 
        print(f"Edad: {self.edad}")
        print(f"Peso: {self.peso}")
        print(F"Tamaño: {self.tamaño}")
        print(f"Vacunado: {self.vacunado}")
        print(f"Esterelizado: {self.esterelizado}")
        print(f"Dueño: {self.dueño}")
        print(f"Collar: {self.collar}")

    def ladrar(self):
        print("El perro ladra")
    def comer(self):
        print("El perro puede comer")
    def correr(self):
        print("El perro puede correr")
    def jugar(self):
        print("El perro puede jugar")
    def dormir(self):
        print("El perro puede dormir")  

perro1=Perro("Max","Labrador","Amarillo","3","30 kg","Grande","Si","No","Juan","Azúl")

