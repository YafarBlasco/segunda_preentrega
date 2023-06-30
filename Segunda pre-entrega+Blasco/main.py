from paquete.modulo1 import Cliente, ClienteVIP
import paquete.modulo2

cliente1 = Cliente("Juan Perez", 30, "Calle Principal 123", "juan@example.com")
print(cliente1)  # Imprime el nombre del cliente

cliente1.realizar_compra("Camisa")  # Realiza una compra
cliente1.actualizar_direccion("Avenida Central 456")  # Actualiza la dirección

cliente2 = ClienteVIP("María López", 35, "Avenida Central 789", "maria@example.com", 100)
print(cliente2)  # Imprime el nombre del cliente VIP

cliente2.realizar_compra("Zapatos")  # Realiza una compra
cliente2.actualizar_direccion("Calle Secundaria 456")  # Actualiza la dirección
cliente2.acumular_puntos(50)  # Acumula puntos