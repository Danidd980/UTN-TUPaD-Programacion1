#Caso 5 – Restaurante – Platos del día y porciones
#listas paralelas
platos = []
porciones = []

print("Bienvenido al sistema de administración de platos del día.")

while True:
    print("\nMenú:")
    print("1. Agregar plato")
    print("2. Consultar porciones de un plato")
    print("3. Listar platos agotados")
    print("4. Vender porciones de un plato")
    print("5. Devolver porciones a un plato")
    print("6. Salir")
    
    opcion = input("Seleccione una opción (1-6): ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del plato: ").strip()
        if nombre == "":
            print("Error: El nombre del plato no puede estar vacío.")
        else:
            cantidad = input("Ingrese la cantidad inicial de porciones: ")
            if cantidad.isdigit():
                cantidad = int(cantidad)
                platos.append(nombre)
                porciones.append(cantidad)
                print("Plato agregado correctamente.")
            else:
                print("Error: La cantidad debe ser un número entero mayor o igual a 0.")

    elif opcion == "2":
        nombre = input("Ingrese el nombre del plato a consultar: ").strip()
        encontrado = False
        for i in range(len(platos)):
            if platos[i].lower() == nombre.lower():
                print("Hay", porciones[i], "porciones disponibles de", platos[i])
                encontrado = True
                break
        if not encontrado:
            print("Plato no encontrado.")

    elif opcion == "3":
        print("Platos agotados:")
        hay_agotados = False
        for i in range(len(platos)):
            if porciones[i] == 0:
                print("-", platos[i])
                hay_agotados = True
        if not hay_agotados:
            print("No hay platos agotados.")

    elif opcion == "4":
        nombre = input("Ingrese el nombre del plato a vender: ").strip()
        cantidad = input("Ingrese la cantidad de porciones a vender: ")
        if cantidad.isdigit():
            cantidad = int(cantidad)
            encontrado = False
            for i in range(len(platos)):
                if platos[i].lower() == nombre.lower():
                    encontrado = True
                    if cantidad <= porciones[i]:
                        porciones[i] -= cantidad
                        print("Venta realizada. Porciones restantes de", platos[i] + ":", porciones[i])
                    else:
                        print("Error: No hay suficientes porciones disponibles.")
                    break
            if not encontrado:
                print("Plato no encontrado.")
        else:
            print("Error: La cantidad debe ser un número entero.")

    elif opcion == "5":
        nombre = input("Ingrese el nombre del plato para devolver porciones: ").strip()
        cantidad = input("Ingrese la cantidad de porciones a devolver: ")
        if cantidad.isdigit():
            cantidad = int(cantidad)
            encontrado = False
            for i in range(len(platos)):
                if platos[i].lower() == nombre.lower():
                    porciones[i] += cantidad
                    print("Devolución realizada. Porciones actuales de", platos[i] + ":", porciones[i])
                    encontrado = True
                    break
            if not encontrado:
                print("Plato no encontrado.")
        else:
            print("Error: La cantidad debe ser un número entero.")

    elif opcion == "6":
        print("Saliendo del sistema. ¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intente nuevamente.")
