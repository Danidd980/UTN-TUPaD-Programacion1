#Caso 6 – Eventos – Entradas por show
shows = []
entradas = []

print("Bienvenido al sistema de gestión de entradas para shows.")

while True:
    print("\nMenú:")
    print("1. Agregar show")
    print("2. Consultar entradas disponibles de un show")
    print("3. Listar shows agotados")
    print("4. Vender entradas")
    print("5. Devolver entradas")
    print("6. Salir")

    opcion = input("Seleccione una opción (1-6): ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del show: ").strip()
        if nombre == "":
            print("Error: El nombre del show no puede estar vacío.")
        else:
            cantidad = input("Ingrese la cantidad de entradas disponibles: ")
            if cantidad.isdigit():
                cantidad = int(cantidad)
                shows.append(nombre)
                entradas.append(cantidad)
                print("Show agregado correctamente.")
            else:
                print("Error: La cantidad debe ser un número entero mayor o igual a 0.")

    elif opcion == "2":
        nombre = input("Ingrese el nombre del show a consultar: ").strip()
        encontrado = False
        for i in range(len(shows)):
            if shows[i].lower() == nombre.lower():
                print("Hay", entradas[i], "entradas disponibles para", shows[i])
                encontrado = True
                break
        if not encontrado:
            print("Show no encontrado.")

    elif opcion == "3":
        print("Shows agotados:")
        hay_agotados = False
        for i in range(len(shows)):
            if entradas[i] == 0:
                print("-", shows[i])
                hay_agotados = True
        if not hay_agotados:
            print("No hay shows agotados.")

    elif opcion == "4":
        nombre = input("Ingrese el nombre del show para vender entradas: ").strip()
        cantidad = input("Ingrese la cantidad de entradas a vender: ")
        if cantidad.isdigit():
            cantidad = int(cantidad)
            encontrado = False
            for i in range(len(shows)):
                if shows[i].lower() == nombre.lower():
                    encontrado = True
                    if cantidad <= entradas[i]:
                        entradas[i] -= cantidad
                        print("Venta realizada. Entradas restantes para", shows[i] + ":", entradas[i])
                    else:
                        print("Error: No hay suficientes entradas disponibles.")
                    break
            if not encontrado:
                print("Show no encontrado.")
        else:
            print("Error: La cantidad debe ser un número entero.")

    elif opcion == "5":
        nombre = input("Ingrese el nombre del show para devolver entradas: ").strip()
        cantidad = input("Ingrese la cantidad de entradas a devolver: ")
        if cantidad.isdigit():
            cantidad = int(cantidad)
            encontrado = False
            for i in range(len(shows)):
                if shows[i].lower() == nombre.lower():
                    entradas[i] += cantidad
                    print("Devolución realizada. Entradas actuales para", shows[i] + ":", entradas[i])
                    encontrado = True
                    break
            if not encontrado:
                print("Show no encontrado.")
        else:
            print("Error: La cantidad debe ser un número entero.")

    elif opcion == "6":
        print("Saliendo del sistema. ¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intente nuevamente.")
