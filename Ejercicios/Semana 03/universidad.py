class Universidad:
    def __init__(self,logo,oferta_educativa,ubicacion,servicios,talleres,salones,num_salones,rector,modalidad,forma_titulación):
        self.logo = logo
        self.oferta_educativa = oferta_educativa
        self.ubicacion = ubicacion
        self.servicios = servicios
        self.talleres = talleres
        self.salones = salones
        self.num_salones = num_salones
        self.rector = rector
        self.modalidad = modalidad
        self.forma_titulación = forma_titulación

        print(f"Logo: {self.logo}")
        print(f"Oferta educativa: {self.oferta_educativa}")
        print(f"Ubicación: {self.ubicacion}")
        print(f"Servicios: {self.servicios}")
        print(f"Talleres: {self.talleres}")
        print(f"Salones: {self.salones}")
        print(f"Número de salones: {self.num_salones}")
        print(f"Rector: {self.rector}")
        print(f"Modalidad: {self.modalidad}")
    
    def inscribir(self):
        print("Se puede inscribir en la universidad.")
    def graduar(self): 
        print("Te puedes graduar de la universidad.")
    def estudiar(self):
        print("Se puede estudiar en la universidad.")
    def aprender(self):
        print("Se puede aprender en la universidad.")
    def jugar(self):
        print("Se puede jugar en la universidad.")
        
utec = Universidad("Logo,jpg", "TICS,Ingeniería Industrial,Ingeniería en Mecatrónica,Contaduría,Desarrollo de negocios, Fisioterapia", "Santiago", "Biblioteca, Cafetería, Psicología", "Taller de voleibol,Futbol,Basquetbol,Guitarra,Danza","Edificio C,K,J", "50", "Tito Dorantes", "Presencial", "Tesina")