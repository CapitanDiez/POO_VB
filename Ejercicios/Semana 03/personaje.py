class PersonajeJuego:
    def __init__(self, nombre, poderes, vestimenta, transformaciones, maestros, familia, edad, enemigos_principales,rival, debilidad):
        self.nombre = nombre
        self.poderes = poderes
        self.vestimenta = vestimenta
        self.transformaciones = transformaciones
        self.maestros = maestros
        self.familia = familia
        self.edad = edad
        self.enemigos_principales = enemigos_principales
        self.rival = rival
        self.debilidad = debilidad

        print(f"Nombre: {self.nombre}")
        print(f"Poderes: {self.poderes}")
        print(f"Vestimenta: {self.vestimenta}")
        print(f"Transformaciones: {self.transformaciones}")
        print(f"Maestros: {self.maestros}")
        print(f"Familia: {self.familia}")
        print(f"Edad: {self.edad}")
        print(f"Enemigos principales: {self.enemigos_principales}")
        print(f"Rival: {self.rival}")
        print(f"Debilidad: {self.debilidad}")



    def atacar(self):
        print("El personaje puede atacar a sus enemigos")

    def defender(self):
        print("El personaje se defiende")

    def transformarse(self):
        print("El personaje se transforma")

    def entrenar(self):
        print("El personaje está entrenando")

    def comer(self):
        print("El personaje está comiendo")


goku = PersonajeJuego("Goku", "Kamehameha", "Gi naranja", "Super Saiyan Dios", "Whis, Roshi", "Gohan, Chi-Chi", 40,"Freezer" "Vegeta", "Cola")
