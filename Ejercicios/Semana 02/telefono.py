class Telefono:
    def __init__(self, marca, modelo, color, precio, almacenamiento, ram, bateria, sistema_operativo, camara, conectividad):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.precio = precio
        self.almacenamiento = almacenamiento
        self.ram = ram
        self.bateria = bateria
        self.sistema_operativo = sistema_operativo
        self.camara = camara
        self.conectividad = conectividad

        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"Precio: {self.precio}")
        print(f"Almacenamiento: {self.almacenamiento}")
        print(f"RAM: {self.ram}")
        print(f"Bateria: {self.bateria}")
        print(f"Sistema Operativo: {self.sistema_operativo}")
        print(f"Camara: {self.camara}")
        print(f"Conectividad: {self.conectividad}")

s24 = Telefono("Samsung", "Galaxy S24 Ultra", "Titanium Black", "$17,500 mxn", "256 GB", "12 GB", "5,000 mAh", "Android 14", "200 MP", "5G")