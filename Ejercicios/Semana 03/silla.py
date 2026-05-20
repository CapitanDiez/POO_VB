class Silla:
    def __init__(self,altura,material,ergonomia,color,forma_base,base,movilidad,diseño,ancho_asiento,reposabrazos):
        self.altura = altura
        self.material = material
        self.ergonomia = ergonomia
        self.color = color
        self.forma_base = forma_base
        self.base = base
        self.movilidad = movilidad
        self.diseño = diseño
        self.ancho_asiento = ancho_asiento
        self.reposabrazos = reposabrazos

        print(f"Altura: {self.altura}")
        print(f"Material: {self.material}")
        print(f"Ergonomía: {self.ergonomia}")
        print(f"Color: {self.color}")
        print(f"Forma de la base: {self.forma_base}")
        print(f"Base: {self.base}")
        print(f"Movilidad: {self.movilidad}")
        print(f"Diseño: {self.diseño}")
        print(f"Ancho del asiento: {self.ancho_asiento}")
        print(f"Reposabrazos: {self.reposabrazos}")

    def reclinarse(self):
        print("La silla se puede reclinar.")
    def girar(self):
        print("La silla puede girar.")
    def mover(self):
        print("La silla se puede mover.")
    def sentarse(self):
        print("Se puede sentar en la silla.")
    def limpiar(self):
        print("La silla se puede limpiar.")

silla1 = Silla("90 cm","Plástico","Si","Negro","Cuadrada","4 patas","Fija","Moderno","45 cm","No")
