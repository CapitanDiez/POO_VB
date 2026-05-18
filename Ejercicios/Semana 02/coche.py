class Coche:
    def __init__(self, marca, modelo, anio, color, puertas, transmision, combustible, traccion, aire_acondicionado, precio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.puertas = puertas
        self.transmision = transmision
        self.combustible = combustible
        self.traccion = traccion
        self.aire_acondicionado = aire_acondicionado
        self.precio = precio

        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.anio}")
        print(f"Color: {self.color}")
        print(f"Puertas: {self.puertas}")
        print(f"Transmision: {self.transmision}")
        print(f"Combustible: {self.combustible}")
        print(f"Traccion: {self.traccion}")
        print(f"Aire acondicionado: {self.aire_acondicionado}")
        print(f"Precio: {self.precio}")

    def arrancar(self):
        print("El coche esta arrancando")

    def abrir_cajuela(self):
        print("La cajuela esta abierta")

    def encender(self):
        print("El aire acondicionado esta encendido")

    def cambiar_marcha(self):
        print("Se ha cambiado la marcha")

    def activar_gps(self):
        print("El GPS esta activando")


coche1 = Coche("Toyota", "Corolla", 2022, "Blanco", 4, "Automatico", "Gasolina", "Delantero", True, 320000)