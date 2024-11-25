# Definición de la clase Estudiante
class Estudiante:
    def __init__(self, nombre, edad, grado):
        """Inicializa un estudiante con nombre, edad, grado y una lista de materias vacía."""
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.materias = []

    def inscribir_materia(self, materia):
        """Agrega una materia a la lista de materias del estudiante."""
        if materia not in self.materias:
            self.materias.append(materia)
            print(f"Materia '{materia}' inscrita para {self.nombre}.")
        else:
            print(f"{self.nombre} ya está inscrito en '{materia}'.")

    def mostrar_materias(self):
        """Muestra las materias inscritas del estudiante."""
        print(f"{self.nombre} está inscrito en las siguientes materias:")
        if self.materias:
            for materia in self.materias:
                print(f"- {materia}")
        else:
            print("No tiene materias inscritas.")

    def actualizar_grado(self, nuevo_grado):
        """Actualiza el grado del estudiante."""
        self.grado = nuevo_grado
        print(f"El grado de {self.nombre} ha sido actualizado a {self.grado}.")

# Programa principal
def main():
    # Crear instancias de estudiantes
    estudiante1 = Estudiante("Santiago", 12, "7°")
    estudiante2 = Estudiante("Messi", 15, "10°")
    estudiante3 = Estudiante("Cristiano", 13, "8°")

    # Mostrar información inicial
    print("Información inicial de los estudiantes:")
    estudiante1.mostrar_materias()
    estudiante2.mostrar_materias()
    estudiante3.mostrar_materias()
    print()

    # Inscribir materias
    estudiante1.inscribir_materia("Matemáticas")
    estudiante1.inscribir_materia("Historia")
    estudiante2.inscribir_materia("Biología")
    estudiante2.inscribir_materia("Matemáticas")
    estudiante3.inscribir_materia("Inglés")
    estudiante3.inscribir_materia("Arte")
    print()

    # Mostrar materias inscritas
    print("Materias inscritas por cada estudiante:")
    estudiante1.mostrar_materias()
    estudiante2.mostrar_materias()
    estudiante3.mostrar_materias()
    print()

    # Actualizar grados
    estudiante1.actualizar_grado("10°")
    estudiante2.actualizar_grado("11°")
    estudiante3.actualizar_grado("9°")
    print()

    # Mostrar información actualizada
    print("Información actualizada de los estudiantes:")
    estudiante1.mostrar_materias()
    estudiante2.mostrar_materias()
    estudiante3.mostrar_materias()

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
