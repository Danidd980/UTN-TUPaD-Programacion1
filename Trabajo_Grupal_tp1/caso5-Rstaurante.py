platos = []
porciones = []

opcion = ""
while opcion != "10":
    print("\n--- Sistema de Gestión de Restaurante ---")
    print("1. Ingresar lista de platos")
    print("2. Ingresar porciones disponibles")
    ("3. Mostrar platos con porciones")
    ("4. Consultar porciones de un plato")
    ("5. Listar platos agotados")
    ("6. Agregar plato")
    ("7. Ver platos agotados")
    ("8. Vender/Devolver porciones")
    ("9. Ver todos los platos")
    ("10. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        platos.clear()
        porciones.clear()
        print("Ingrese los nombres de los platos (ingrese 'fin' para terminar):")
        while True:
            nombre = input("Plato: ")
            if nombre.lower() == 'fin':
                break
            platos.append(nombre)

    elif opcion == "2":
        if len(platos) > 0:
            porciones.clear()
            for plato in platos:
                cantidad = int(input(f"Porciones para '{plato}': "))
                porciones.append(cantidad)
        else:
            print("No hay platos para asignar porciones.")

    elif opcion == "3" or opcion == "9":
        for i in range(len(platos)):
            print(f"{platos[i]}: {porciones[i]} porciones")

    elif opcion == "4":
        nombre = input("Ingrese el nombre del plato: ")
        if nombre in platos:
            indice = platos.index(nombre)
            print(f"'{nombre}' tiene {porciones[indice]} porciones.")
        else:
            print("Plato no encontrado.")

    elif opcion == "5" or opcion == "7":
        print("--- Platos Agotados ---")
        for i in range(len(platos)):
            if porciones[i] == 0:
                print(f"- {platos[i]}")

    elif opcion == "6":
        nombre = input("Nombre del nuevo plato: ")
        cantidad = int(input(f"Porciones para '{nombre}': "))
        platos.append(nombre)
        porciones.append(cantidad)
        print("Plato agregado.")

    elif opcion == "8":
        nombre = input("Plato a actualizar: ")
        if nombre in platos:
            indice = platos.index(nombre)
            op = input("¿Vender (V) o devolver (D)?: ").upper()
            cantidad = int(input("Cantidad: "))
            
            if op == "V":
                porciones[indice] -= cantidad
            elif op == "D":
                porciones[indice] += cantidad
            print("Actualización realizada.")
        else:
            print("Plato no encontrado.")
            
    elif opcion == "10":
        print("Saliendo...")

    else:
        print("Opción no válida.")