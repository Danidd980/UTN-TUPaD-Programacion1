#Caso 5 – Restaurante – Platos del día y porciones
# Listas paralelas
platos = []
porciones = []

opcion = ""
while opcion != "10":
    print("\n===== MENÚ DEL DÍA =====")
    print("1. Ingresar lista de platos")
    print("2. Ingresar porciones disponibles")
    print("3. Mostrar platos con porciones")
    print("4. Consultar porciones de un plato")
    print("5. Listar platos agotados")
    print("6. Agregar plato")
    print("7. Ver platos agotados")
    print("8. Vender/Devolver porciones")
    print("9. Ver todos los platos")
    print("10. Salir")
    
    opcion = input("Seleccione una opción (1-10): ")

    if opcion == "1":
        print("\n--- Ingresar lista de platos ---")
        continuar = "s"
        while continuar == "s":
            plato = input("Ingrese el nombre del plato (o ENTER para terminar): ")
            if plato != "":
                platos.append(plato)
                porciones.append(0)
            else:
                print("Nombre no válido.")
            continuar = input("¿Desea ingresar otro plato? (s/n): ")

    elif opcion == "2":
        print("\n--- Ingresar porciones disponibles ---")
        if len(platos) == 0:
            print("Primero debe ingresar los platos.")
        else:
            i = 0
            while i < len(platos):
                cantidad = input("Ingrese porciones para '" + platos[i] + "': ")
                if cantidad.isdigit():
                    porciones[i] = int(cantidad)
                    i += 1
                else:
                    print("Por favor, ingrese un número válido (≥ 0).")

    elif opcion == "3":
        print("\n--- Platos con porciones disponibles ---")
        i = 0
        while i < len(platos):
            print(platos[i] + ": " + str(porciones[i]) + " porciones")
            i += 1

    elif opcion == "4":
        print("\n--- Consultar porciones de un plato ---")
        nombre = input("Ingrese el nombre del plato: ")
        i = 0
        encontrado = False
        while i < len(platos):
            if platos[i] == nombre:
                print(nombre + ": " + str(porciones[i]) + " porciones disponibles")
                encontrado = True
            i += 1
        if not encontrado:
            print("El plato no se encuentra en el menú.")

    elif opcion == "5" or opcion == "7":
        print("\n--- Platos agotados ---")
        i = 0
        agotados = False
        while i < len(porciones):
            if porciones[i] == 0:
                print(platos[i])
                agotados = True
            i += 1
        if not agotados:
            print("No hay platos agotados.")

    elif opcion == "6":
        print("\n--- Agregar nuevo plato ---")
        nuevo = input("Ingrese el nombre del nuevo plato: ")
        if nuevo == "":
            print("Nombre no válido.")
        else:
            existe = False
            i = 0
            while i < len(platos):
                if platos[i] == nuevo:
                    existe = True
                i += 1
            if existe:
                print("Este plato ya existe en el menú.")
            else:
                cantidad = input("Ingrese cantidad inicial de porciones para '" + nuevo + "': ")
                if cantidad.isdigit():
                    platos.append(nuevo)
                    porciones.append(int(cantidad))
                    print("Plato '" + nuevo + "' agregado con " + cantidad + " porciones.")
                else:
                    print("Cantidad inválida. No se agregó el plato.")

    elif opcion == "8":
        print("\n--- Vender/Devolver porciones ---")
        nombre = input("Ingrese el nombre del plato: ")
        i = 0
        encontrado = False
        while i < len(platos):
            if platos[i] == nombre:
                encontrado = True
                accion = input("¿Desea 'vender' o 'devolver' porciones?: ")
                cantidad = input("Ingrese la cantidad: ")
                if cantidad.isdigit():
                    cantidad = int(cantidad)
                    if accion == "vender":
                        if cantidad <= porciones[i]:
                            porciones[i] = porciones[i] - cantidad
                            print("Se vendieron", cantidad, "porciones. Ahora quedan", porciones[i])
                        else:
                            print("No hay suficientes porciones disponibles.")
                    elif accion == "devolver":
                        porciones[i] = porciones[i] + cantidad
                        print("Se devolvieron", cantidad, "porciones. Ahora hay", porciones[i])
                    else:
                        print("Acción no válida.")
                else:
                    print("Cantidad no válida.")
            i += 1
        if not encontrado:
            print("El plato no se encuentra en el menú.")

    elif opcion == "9":
        print("\n--- Todos los platos ---")
        i = 0
        while i < len(platos):
            print(platos[i] + ": " + str(porciones[i]) + " porciones")
            i += 1

    elif opcion == "10":
        print("Saliendo del programa. ¡Hasta luego!")
    else:
        print("Opción no válida. Intente de nuevo.")
