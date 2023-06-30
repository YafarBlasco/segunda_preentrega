import json

def registrar_usuario():
    print("Registro de Usuario")
    nombre = input("Ingresa su nombre de usuario: ")
    contraseña = input("Ingresa su contraseña: ")

    usuario = {
        "nombre": nombre,
        "contraseña": contraseña
    }

    return usuario

def almacenar_usuario(usuario, base_datos):
    base_datos.append(usuario)
    print("Usuario registrado exitosamente.")

def iniciar_sesion(base_datos):
    print("Iniciar Sesión")
    nombre = input("Ingresa su nombre de usuario: ")
    contraseña = input("Ingresa su contraseña: ")

    for usuario in base_datos:
        if usuario["nombre"] == nombre and usuario["contraseña"] == contraseña:
            print("Inicio de sesión exitoso.")
            return

    print("Nombre de usuario o contraseña incorrectos.")

def mostrar_usuarios(base_datos):
    print("\nUsuarios registrados:")
    for usuario in base_datos:
        print(f"Nombre: {usuario['nombre']}")

# Base de datos para almacenar los usuarios
base_datos_usuarios = []

while True:
    print("\n--- Menú ---")
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Mostrar usuarios registrados")
    print("4. Salir")

    opcion = input("Ingresa una opción: ")

    if opcion == "1":
        nuevo_usuario = registrar_usuario()
        almacenar_usuario(nuevo_usuario, base_datos_usuarios)
    elif opcion == "2":
        iniciar_sesion(base_datos_usuarios)
    elif opcion == "3":
        mostrar_usuarios(base_datos_usuarios)
    elif opcion == "4":
        print("Hasta luego")
        break
    else:
        print("Opción inválida. Por favor, ingresa una opción válida.")

# base de datos a JSON
with open("usuarios.json", "w") as archivo:
    json.dump(base_datos_usuarios, archivo)