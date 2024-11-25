# Definición de la clase Libro
class Libro:
    def __init__(self, titulo, autor, genero, precio):
        """Inicializa un libro con título, autor, género y precio."""
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        """Aplica un descuento al precio del libro."""
        if 0 < porcentaje <= 100:
            descuento = self.precio * (porcentaje / 100)
            self.precio -= descuento
            print(f"Se ha aplicado un descuento del {porcentaje}% al libro '{self.titulo}'. Precio actual: ${self.precio:.2f}")
        else:
            print("El porcentaje de descuento debe estar entre 0 y 100.")

    def mostrar_informacion(self):
        """Imprime los detalles del libro."""
        print(f"Libro: {self.titulo}")
        print(f"  Autor: {self.autor}")
        print(f"  Género: {self.genero}")
        print(f"  Precio: ${self.precio:.2f}")

    def es_mas_caro_que(self, otro_libro):
        """Compara precios entre dos libros y devuelve el libro más caro."""
        if self.precio > otro_libro.precio:
            print(f"'{self.titulo}' es más caro que '{otro_libro.titulo}'.")
            return self
        elif self.precio < otro_libro.precio:
            print(f"'{otro_libro.titulo}' es más caro que '{self.titulo}'.")
            return otro_libro
        else:
            print(f"'{self.titulo}' y '{otro_libro.titulo}' tienen el mismo precio.")
            return None

# Programa principal
def main():
    # Crear instancias de libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 20.00)
    libro2 = Libro("1984", "George Orwell", "Distopía", 15.00)
    libro3 = Libro("El Principito", "Antoine de Saint-Exupéry", "Fábula", 10.00)

    # Mostrar información inicial de los libros
    print("Información inicial de los libros:")
    libro1.mostrar_informacion()
    libro2.mostrar_informacion()
    libro3.mostrar_informacion()
    print()

    # Aplicar descuentos a los libros
    print("Aplicando descuentos:")
    libro1.aplicar_descuento(10)  # 10% de descuento
    libro2.aplicar_descuento(20)  # 20% de descuento
    libro3.aplicar_descuento(5)   # 5% de descuento
    print()

    # Comparar precios entre libros
    print("Comparando precios:")
    libro1.es_mas_caro_que(libro2)
    libro2.es_mas_caro_que(libro3)
    libro1.es_mas_caro_que(libro3)
    print()

    # Mostrar información actualizada de los libros
    print("Información final de los libros:")
    libro1.mostrar_informacion()
    libro2.mostrar_informacion()
    libro3.mostrar_informacion()

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
