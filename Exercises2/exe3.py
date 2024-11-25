# Definición de la clase Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, año, kilometraje):
        """Inicializa un vehículo con marca, modelo, año y kilometraje."""
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje

    def conducir(self, distancia):
        """Incrementa el kilometraje del vehículo."""
        if distancia > 0:
            self.kilometraje += distancia
            print(f"El vehículo {self.marca} {self.modelo} ha recorrido {distancia} km. Kilometraje total: {self.kilometraje} km.")
        else:
            print("La distancia debe ser un valor positivo.")

    def mostrar_detalles(self):
        """Imprime todos los detalles del vehículo."""
        print(f"Vehículo: {self.marca} {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Kilometraje: {self.kilometraje} km")

    def es_vehiculo_antiguo(self):
        """Devuelve True si el vehículo tiene más de 20 años."""
        from datetime import datetime
        año_actual = datetime.now().year
        return (año_actual - self.año) > 20

# Programa principal
def main():
    # Crear instancias de vehículos
    vehiculo1 = Vehiculo("Toyota", "Corolla", 1995, 180000)
    vehiculo2 = Vehiculo("Ford", "Fiesta", 2010, 90000)
    vehiculo3 = Vehiculo("Honda", "Civic", 2021, 15000)

    # Mostrar detalles iniciales
    print("Detalles iniciales de los vehículos:")
    vehiculo1.mostrar_detalles()
    vehiculo2.mostrar_detalles()
    vehiculo3.mostrar_detalles()
    print()

    # Conducir los vehículos
    vehiculo1.conducir(150)
    vehiculo2.conducir(500)
    vehiculo3.conducir(1200)
    print()

    # Verificar si son vehículos antiguos
    print(f"¿El {vehiculo1.marca} {vehiculo1.modelo} es antiguo? {'Sí' if vehiculo1.es_vehiculo_antiguo() else 'No'}")
    print(f"¿El {vehiculo2.marca} {vehiculo2.modelo} es antiguo? {'Sí' if vehiculo2.es_vehiculo_antiguo() else 'No'}")
    print(f"¿El {vehiculo3.marca} {vehiculo3.modelo} es antiguo? {'Sí' if vehiculo3.es_vehiculo_antiguo() else 'No'}")
    print()

    # Mostrar detalles finales
    print("Detalles finales de los vehículos:")
    vehiculo1.mostrar_detalles()
    vehiculo2.mostrar_detalles()
    vehiculo3.mostrar_detalles()

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
