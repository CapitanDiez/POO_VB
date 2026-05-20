class Mesa:
    def __init__(self,altura,forma,precio,material,peso,uso,color,ancho,largo,estabilidad):
        self.altura = altura
        self.forma = forma
        self.precio = precio
        self.material = material
        self.peso = peso
        self.uso = uso
        self.color = color
        self.ancho = ancho
        self.largo = largo
        self.estabilidad = estabilidad

        print(f"Altura: {self.altura}")
        print(f"Forma: {self.forma}")
        print(f"Precio: {self.precio}")
        print(f"Material: {self.material}")
        print(f"Peso: {self.peso}")
        print(f"Uso: {self.uso}")
        print(f"Color: {self.color}")
        print(f"Ancho: {self.ancho}")
        print(f"Largo: {self.largo}")
        print(f"Estabilidad: {self.estabilidad}")
    
    def sostener(self):
        print("La mesa sostiene objetos.")
    def mover(self):
        print("La mesa se puede mover.")
    def ensamblar(self):
        print("La mesa se puede ensamblar.")
    def limpiar(self):
        print("La mesa se puede limpiar.")
    def desarmar(self):
        print("La mesa se puede desarmar.")

mesa1 = Mesa("75 cm", "Rectangular", "$1500 mxn", "Madera", "15 kg", "Comedor", "Café", "50 cm", "120 cm", "Alta")