#Caso 7 – Educación – Estudiantes y asistencias
alumnos = []
asistencias = []

opcion = ""
while opcion != "5":
    print("\n--- Sistema de Asistencia de Alumnos ---")
    print("1. Agregar estudiante")
    print("2. Ver asistencia de un estudiante")
    print("3. Listar estudiantes con 0 asistencias")
    print("4. Marcar asistencia")
    print("5. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        # Agregar estudiante
        nombre_estudiante = input("Ingrese el nombre del estudiante: ")
        while not nombre_estudiante.strip():
            print("El nombre no puede estar vacío.")
            nombre_estudiante = input("Ingrese el nombre del estudiante: ")
            
        alumnos.append(nombre_estudiante)
        asistencias.append(0)
        print(f"Estudiante '{nombre_estudiante}' agregado con 0 asistencias.")

    elif opcion == "2":
        # Ver asistencia
        nombre_estudiante = input("Ingrese el nombre del estudiante a consultar: ")
        encontrado = False
        for i in range(len(alumnos)):
            if alumnos[i] == nombre_estudiante:
                print(f"'{alumnos[i]}' tiene {asistencias[i]} asistencias.")
                encontrado = True
                break
        if not encontrado:
            print(f"El estudiante '{nombre_estudiante}' no se encuentra en el sistema.")

    elif opcion == "3":
        # Listar estudiantes con 0 asistencias
        print("\n--- Estudiantes con 0 Asistencias ---")
        ninguno_cero = True
        for i in range(len(alumnos)):
            if asistencias[i] == 0:
                print(f"- {alumnos[i]}")
                ninguno_cero = False
        if ninguno_cero:
            print("Todos los estudiantes tienen al menos 1 asistencia.")

    elif opcion == "4":
        # Marcar asistencia
        nombre_estudiante = input("Ingrese el nombre del estudiante para marcar asistencia: ")
        encontrado = False
        for i in range(len(alumnos)):
            if alumnos[i] == nombre_estudiante:
                asistencias[i] += 1
                print(f"Asistencia marcada para '{alumnos[i]}'. Asistencias totales: {asistencias[i]}")
                encontrado = True
                break
        if not encontrado:
            print(f"El estudiante '{nombre_estudiante}' no se encuentra en el sistema.")
            
    elif opcion == "5":
        print("Saliendo del sistema de asistencia.")

    else:
        print("Opción no válida. Por favor, intente de nuevo.")