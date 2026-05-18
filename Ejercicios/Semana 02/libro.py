class Libro:
    def __init__(self, titulo, autor, editorial, anio, genero, idioma, paginas, isbn, disponible, ubicacion):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.anio = anio
        self.genero = genero
        self.idioma = idioma
        self.paginas = paginas
        self.isbn = isbn
        self.disponible = disponible
        self.ubicacion = ubicacion
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Editorial: {self.editorial}")
        print(f"Año: {self.anio}")
        print(f"Genero: {self.genero}")
        print(f"Idioma: {self.idioma}")
        print(f"Paginas: {self.paginas}")
        print(f"ISBN: {self.isbn}")
        print(f"Disponible: {self.disponible}")
        print(f"Ubicacion: {self.ubicacion}")

    def entretener(self):
        print("Entreteniendo")

    def leer(self):
        print("Leer")

    def comprender(self):
        print("Comprender")

    def reflexionar(self):
        print("Reflexionando")

    def aprender(self):
        print("Aprender")


libro = Libro("El Principito", "Antoine de Saint-Exupery", "Gallimard", 1943, "Literatura Infantil", "Español", 96, "978-607-07-0059-8", "No", "Estante B2")

