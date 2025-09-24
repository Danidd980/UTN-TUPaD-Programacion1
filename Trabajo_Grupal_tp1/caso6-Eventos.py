#Caso 6 – Eventos – Entradas por show
shows = []
entradas = []

opcion = ""
while opcion != "5":
    print("\n--- Sistema de Gestión de Shows ---")
    print("1. Agregar show")
    print("2. Consultar entradas")
    print("3. Listar shows agotados")
    print("4. Actualizar entradas")
    print("5. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        # Agregar show
        nombre_show = input("Ingrese el nombre del show: ")
        cantidad_entradas = int(input("Ingrese la cantidad de entradas: "))
        
        shows.append(nombre_show)
        entradas.append(cantidad_entradas)
        print("Show agregado exitosamente.")

    elif opcion == "2":
        # Consultar entradas
        nombre_show = input("Ingrese el nombre del show a consultar: ")
        
        # Buscar el show en la lista
        encontrado = False
        for i in range(len(shows)):
            if shows[i] == nombre_show:
                print(f"El show '{shows[i]}' tiene {entradas[i]} entradas disponibles.")
                encontrado = True
                break
        
        if not encontrado:
            print("El show no se encuentra en el sistema.")

    elif opcion == "3":
        # Listar shows agotados
        print("\n--- Shows Agotados ---")
        for i in range(len(shows)):
            if entradas[i] == 0:
                print(f"- {shows[i]}")

    elif opcion == "4":
        # Actualizar entradas
        nombre_show = input("Ingrese el nombre del show a actualizar: ")
        
        encontrado = False
        for i in range(len(shows)):
            if shows[i] == nombre_show:
                encontrado = True
                print(f"Entradas actuales para '{shows[i]}': {entradas[i]}")
                
                tipo_op = input("¿Vender (V) o devolver (D)?: ")
                cantidad = int(input("Ingrese la cantidad: "))

                if tipo_op.upper() == "V":
                    if cantidad <= entradas[i]:
                        entradas[i] -= cantidad
                        print("Venta realizada.")
                    else:
                        print("No hay suficientes entradas.")
                elif tipo_op.upper() == "D":
                    entradas[i] += cantidad
                    print("Devolución realizada.")
                else:
                    print("Operación no válida.")
                break

        if not encontrado:
            print("El show no se encuentra en el sistema.")

    elif opcion == "5":
        print("Saliendo del sistema.")

    else:
        print("Opción no válida. Intente de nuevo.")