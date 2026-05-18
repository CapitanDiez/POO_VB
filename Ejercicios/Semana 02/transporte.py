class Transporte:
    def __init__(self, marca, modelo, anio, color, velocidad, peso, capacidad, combustible, pais, precio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.velocidad = velocidad
        self.peso = peso
        self.capacidad = capacidad
        self.combustible = combustible
        self.pais = pais
        self.precio = precio
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.anio}")
        print(f"Color: {self.color}")
        print(f"Velocidad: {self.velocidad}")
        print(f"Peso: {self.peso}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Combustible: {self.combustible}")
        print(f"Pais: {self.pais}")
        print(f"Precio: {self.precio}")

    def arrancar(self):
        print("El transporte esta arrancando")

    def frenar(self):
        print("El transporte esta frenando")

    def acelerar(self):
        print("El transporte esta acelerando")

    def detener(self):
        print("El transporte se ha detenido")

    def recargar_combustible(self):
        print("El transporte esta recargando combustible")


transporte1 = Transporte("Ford", "Transit", 2021, "Gris", 140, 2500, 15, "Diesel", "Mexico", 450000)

print(f"Marca: {transporte1.marca}")
print(f"Modelo: {transporte1.modelo}")
print(f"Año: {transporte1.anio}")
print(f"Color: {transporte1.color}")
print(f"Velocidad: {transporte1.velocidad}")
print(f"Peso: {transporte1.peso}")
print(f"Capacidad: {transporte1.capacidad}")
print(f"Combustible: {transporte1.combustible}")
print(f"Pais: {transporte1.pais}")
print(f"Precio: {transporte1.precio}")