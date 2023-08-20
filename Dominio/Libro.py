from Material import Material


class Libro(Material):
    contador_libro = 0

    def __init__(self, codigo: str, autor: str, titulo: str, anio: int, editorial: str, disponible: bool,
                 cantidad_disponible: int, tipo_pasta: str):
        super().__init__(codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible)
        self._tipo_pasta = tipo_pasta
        Libro.contador_libro += 1

    @property
    def tipo_pasta(self):
        return self._tipo_pasta

    @tipo_pasta.setter
    def tipo_pasta(self, tipo_pasta):
        self._tipo_pasta = tipo_pasta

    def actualizar_disponibilidad(self, disponible):
        self.disponible = disponible


if __name__ == "__main__":
    libro1 = Libro("12345", "Jame Yepez", "Libro CULPABLES", 2023, "Editorial 345", True, 10, "Tapa dura")
    libro2 = Libro("67890", "Dome Anchundia", "Libro ORGULLO Y PREJUICIO", 2022, "Editorial 890J8", False, 5,
                   "Tapa blanda")

    # Acceder a los atributos de los libros
    print(libro1.codigo)
    print(libro1.titulo)
    print(libro1.autor)
    print(libro1.anio)
    print(libro1.editorial)
    print(libro1.disponible)
    print(libro1.cantidad_disponible)
    print(libro1.tipo_pasta)
    print()

    print(libro2.codigo)
    print(libro2.titulo)
    print(libro2.autor)
    print(libro2.anio)
    print(libro2.editorial)
    print(libro2.disponible)
    print(libro2.cantidad_disponible)
    print(libro2.tipo_pasta)
    print()

    # Modificar atributos
    libro1.actualizar_disponibilidad(False)
    libro2.tipo_pasta = "Pasta dura"

    # Acceder a los atributos modificados
    print(libro1.disponible)
    print(libro2.tipo_pasta)
    print()

    # Acceder al contador de libros
    print(Libro.contador_libro)


'''
Integrantes grupo 15:
Darling medina Chalen 
Bryan Revelo Yagual
Katherine Sanchez Silva
'''