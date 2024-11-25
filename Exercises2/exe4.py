# Definición de la clase Habitacion
class Habitacion:
    def __init__(self, numero, tipo, precio):
        """Inicializa una habitación con su número, tipo, precio y estado disponible."""
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def reservar(self):
        """Marca la habitación como no disponible si está libre."""
        if self.disponible:
            self.disponible = False
            print(f"La habitación {self.numero} ha sido reservada.")
        else:
            print(f"La habitación {self.numero} ya está reservada.")

    def liberar(self):
        """Marca la habitación como disponible si está ocupada."""
        if not self.disponible:
            self.disponible = True
            print(f"La habitación {self.numero} ahora está disponible.")
        else:
            print(f"La habitación {self.numero} ya está disponible.")

    def mostrar_informacion(self):
        """Imprime todos los detalles de la habitación."""
        estado = "Disponible" if self.disponible else "Reservada"
        print(f"Habitación {self.numero}:")
        print(f"  Tipo: {self.tipo}")
        print(f"  Precio: ${self.precio:.2f}")
        print(f"  Estado: {estado}")

# Programa principal
def main():
    # Crear instancias de habitaciones
    habitacion1 = Habitacion(101, "Individual", 50.00)
    habitacion2 = Habitacion(102, "Doble", 75.00)
    habitacion3 = Habitacion(103, "Suite", 120.00)

    # Mostrar información inicial de las habitaciones
    print("Estado inicial de las habitaciones:")
    habitacion1.mostrar_informacion()
    habitacion2.mostrar_informacion()
    habitacion3.mostrar_informacion()
    print()

    # Reservar habitaciones
    print("Reservando habitaciones:")
    habitacion1.reservar()
    habitacion2.reservar()
    habitacion1.reservar()  # Intento de reservar nuevamente
    print()

    # Mostrar información después de las reservas
    print("Estado después de las reservas:")
    habitacion1.mostrar_informacion()
    habitacion2.mostrar_informacion()
    habitacion3.mostrar_informacion()
    print()

    # Liberar habitaciones
    print("Liberando habitaciones:")
    habitacion1.liberar()
    habitacion2.liberar()
    habitacion2.liberar()  # Intento de liberar nuevamente
    print()

    # Mostrar información final de las habitaciones
    print("Estado final de las habitaciones:")
    habitacion1.mostrar_informacion()
    habitacion2.mostrar_informacion()
    habitacion3.mostrar_informacion()

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
