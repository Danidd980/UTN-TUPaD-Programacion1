"""lista donde se guardaran los textos y la cantidad de ejemplares"""
texto = []  
ejemplares = []  

"""opciones del menu"""
def agregar_titulo():
    titulo = input("Ingrese el título del libro: ").strip()
    if titulo == "":
        print("El título no puede estar vacío.")
        return
    if titulo in texto:
        print("Ese título ya existe en el catálogo.")
        return
    try:
        cantidad = int(input("Ingrese la cantidad de ejemplares: "))
        if cantidad < 0:
            print("La cantidad no puede ser negativa.")
            return
    except ValueError:
        print("Debe ingresar un número entero.")
        return
    texto.append(titulo)
    ejemplares.append(cantidad)
    print(f"'{titulo}' agregado con {cantidad} ejemplares.")

def consultar_disponibilidad():
    titulo = input("Ingrese el título a consultar: ").strip()
    if titulo in texto:
        i = texto.index(titulo)
        print(f"'{titulo}' tiene {ejemplares[i]} ejemplares disponibles.")
    else:
        print("Ese título no existe en el catálogo.")

def ver_agotados():
    print("Libros sin ejemplares disponibles:")
    agotados = False
    for i in range(len(texto)):
        if ejemplares[i] == 0:
            print(f"- {texto[i]}")
            agotados = True
    if not agotados:
        print("No hay libros agotados.")

def prestar_libro():
    titulo = input("Ingrese el título a prestar: ").strip()
    if titulo in texto:
        i = texto.index(titulo)
        if ejemplares[i] > 0:
            ejemplares[i] -= 1
            print(f"Se prestó un ejemplar de '{titulo}'. Quedan {ejemplares[i]}.")
        else:
            print("No hay ejemplares disponibles para prestar.")
    else:
        print("Ese título no existe en el catálogo.")

def devolver_libro():
    titulo = input("Ingrese el título a devolver: ").strip()
    if titulo in texto:
        i = texto.index(titulo)
        try:
            cantidad = int(input("Ingrese la cantidad de ejemplares a devolver: "))
            if cantidad < 1:
                print("La cantidad debe ser al menos 1.")
                return
        except ValueError:
            print("Debe ingresar un número entero.")
            return
        ejemplares[i] += cantidad
        print(f"Se devolvieron {cantidad} ejemplares de '{titulo}'. Total: {ejemplares[i]}.")
    else:
        print("Ese título no existe en el catálogo.")

def ver_catalogo():
    print("Catálogo completo de la biblioteca:")
    for i in range(len(texto)):
        print(f"- {texto[i]}: {ejemplares[i]} ejemplares")


"""MENU"""
def menu():
    while True:
        print("\n--- MENÚ DE LA BIBLIOTECA ---")
        print("1. Agregar título")
        print("2. Consultar disponibilidad")
        print("3. Ver agotados")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Ver catálogo completo")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_titulo()
        elif opcion == "2":
            consultar_disponibilidad()
        elif opcion == "3":
            ver_agotados()
        elif opcion == "4":
            prestar_libro()
        elif opcion == "5":
            devolver_libro()
        elif opcion == "6":
            ver_catalogo()
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu()