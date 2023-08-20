from Dominio.Material import Material


class Revista(Material):
    contador_revista = 0

    def __init__(self, codigo: str, autor: str, titulo: str, anio: int, editorial: str, disponible: bool,
                 cantidad_disponible: int, tipo: str):
        super().__init__(codigo, autor, titulo, anio, editorial, disponible, cantidad_disponible)
        self._tipo = tipo
        Revista.contador_revista += 1

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    def actualizar_disponibilidad(self, disponible):
        self.disponible = disponible


if __name__ == "__main__":
    revista = Revista("09456", "Jame Yepez", "Revista Espejo", 2023, "Editorial 908", True, 10, "Moda")
    revista2 = Revista("67890", "Dome Anchundia", "Revista Tecnology", 2022, "Editorial 876", False, 5, "Tecnología")
    revista3 = Revista("36533", "Livintong Gallardo", "Revista De Inteligencia Artificial", 2021, "Editorial 430",
                       False, 8, "Inteligencia Artificial")
    print(revista.titulo)
    print(revista2.titulo)
    print(revista3.titulo)
    revista.actualizar_disponibilidad(False)
    revista2.actualizar_disponibilidad(False)
    revista3.actualizar_disponibilidad(True)
    print("Disponibilidad actual revista 1")
    print(revista.disponible)
    print("Disponibilidad actual revista 2")
    print(revista2.disponible)
    print("Disponibilidad actual revista 3")
    print(revista3.disponible)
    print("Revistas existentes")
    print(Revista.contador_revista)


'''
Integrantes grupo 15:
Darling medina Chalen 
Bryan Revelo Yagual
Katherine Sanchez Silva
'''