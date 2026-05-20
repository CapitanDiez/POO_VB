class Alumno:
    def __init__(self,nombre,carrera,edad,cuatrimestre,grupo,taller,seleccion_deportiva,materias,promedio,salon):
        self.nombre=nombre
        self.carrera=carrera
        self.edad=edad
        self.cuatrimestre=cuatrimestre
        self.grupo=grupo
        self.taller=taller
        self.seleccion_deportiva=seleccion_deportiva
        self.materias=materias
        self.promedio=promedio
        self.salon=salon

        print(f"Nombre: {self.nombre}")
        print(f"Carrera: {self.carrera}")
        print(f"Edad:{self.edad}")
        print(f"Cuatrimestre: {self.cuatrimestre}")
        print(f"Grupo: {self.grupo}")
        print(f"Taller: {self.taller}")
        print(f"Selección deportiva: {self.seleccion_deportiva}")
        print(f"Materias: {self.materias}")
        print(f"Promedio: {self.promedio}")
        print(f"Salón: {self.salon}")

        def estudiar(self):
            print("Victor puede estudiar")
        def leer(self):
            print("Se puede leer libros")
        def aprender(self):
            print("Se pueden aprender cosas nuevas")
        def reprobar(self):
            print("Victor puede reprobar materias")
        def Aprobar(self):
            print("Se pueden aprobar materias")
     
        

victor=Alumno("Victor", "TICS","24","Tercero","32","Voleibol","Voleibol","Inglés,Cálculo,Programación,Bases de datos","9,2")
        