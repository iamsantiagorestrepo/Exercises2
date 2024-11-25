# Definición de la clase Producto
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def actualizar_precio(self, nuevo_precio):
        """Actualiza el precio del producto."""
        self.precio = nuevo_precio
        print(f"El precio del producto '{self.nombre}' se ha actualizado a ${self.precio}.")

    def ajustar_inventario(self, cambio_cantidad):
        """Ajusta el inventario del producto, permitiendo incrementos o decrementos."""
        self.cantidad += cambio_cantidad
        accion = "incrementado" if cambio_cantidad > 0 else "disminuido"
        print(f"La cantidad de '{self.nombre}' se ha {accion} en {abs(cambio_cantidad)} unidades. Total: {self.cantidad}.")

    def mostrar_informacion(self):
        """Muestra los detalles del producto."""
        print(f"Producto: {self.nombre}, Precio: ${self.precio}, Cantidad: {self.cantidad} unidades.")

# Programa principal
def main():

    # Crear instancias de productos
    producto1 = Producto("Agua", 1200, 50)
    producto2 = Producto("Cerveza", 2000, 30)
    producto3 = Producto("Mekato", 3000, 20)

    # Mostrar información inicial
    print("Información inicial de los productos:")
    producto1.mostrar_informacion()
    producto2.mostrar_informacion()
    producto3.mostrar_informacion()
    print()

    # Actualizar precios
    producto1.actualizar_precio(1300)
    producto2.actualizar_precio(1800)
    print()

    # Ajustar inventarios
    producto1.ajustar_inventario(1000)  # Incrementar
    producto3.ajustar_inventario(500)  # Disminuir
    print()

    # Mostrar información final
    print("Información actualizada de los productos:")
    producto1.mostrar_informacion()
    producto2.mostrar_informacion()
    producto3.mostrar_informacion()

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
