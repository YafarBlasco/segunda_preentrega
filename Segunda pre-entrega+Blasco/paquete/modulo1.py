class Cliente:
    def __init__(self, nombre, edad, direccion, correo):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.correo = correo

    def __str__(self):
        return self.nombre

    def realizar_compra(self, producto):
        print(f"{self.nombre} ha realizado la compra del producto {producto}")

    def actualizar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion
        print(f"{self.nombre} ha actualizado su dirección a {nueva_direccion}")


class ClienteVIP(Cliente):
    def __init__(self, nombre, edad, direccion, correo, puntos):
        super().__init__(nombre, edad, direccion, correo)
        self.puntos = puntos

    def acumular_puntos(self, cantidad):
        self.puntos += cantidad
        print(f"{self.nombre} ha acumulado {cantidad} puntos. Total de puntos: {self.puntos}")