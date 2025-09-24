"""Caso 2 _ Clinica_ turnos por especialidad(cupos por dia)"""
"""listas de especialidades y cupos"""
especialidades = [] 
cupos = []  

"""opciones de MENU"""
def agregar_especialidad():
    especialidad = input("Ingrese la especialidad: ").strip()
    if especialidad == "":
        print("La especialidad no puede estar vacía.")
        return
    if especialidad in especialidades:
        print("Esa especialidad ya existe en la clínica.")
        return
    try:
        cantidad_cupos = int(input("Ingrese la cantidad de cupos: "))
        if cantidad_cupos < 0:
            print("La cantidad de cupos no puede ser negativa.")
            return
    except ValueError:
        print("Debe ingresar un número entero.")
        return
    especialidades.append(especialidad)
    cupos.append(cantidad_cupos)
    print(f"'{especialidad}' agregada con {cantidad_cupos} cupos.")

def consultar_cupos():
    especialidad = input("Ingrese la especialidad a consultar: ").strip()
    if especialidad in especialidades:
        i = especialidades.index(especialidad)
        print(f"'{especialidad}' tiene {cupos[i]} cupos disponibles.")
    else:
        print("Esa especialidad no existe en la clínica.")

def ver_especialidades():
    print("Especialidades de la clínica:")
    for i in range(len(especialidades)):
        print(f"{especialidades[i]}: {cupos[i]} cupos")

def agregar_cupos():
    especialidad = input("Ingrese la especialidad a agregar cupos: ").strip()
    if especialidad in especialidades:
        i = especialidades.index(especialidad)
        try:
            cantidad_cupos = int(input("Ingrese la cantidad de cupos a agregar: "))
            if cantidad_cupos < 0:
                print("La cantidad de cupos no puede ser negativa.")
                return
        except ValueError:
            print("Debe ingresar un número entero.")
            return
        cupos[i] += cantidad_cupos
        print(f"Se agregaron {cantidad_cupos} cupos a '{especialidad}'. Total: {cupos[i]} cupos.")
    else:
        print("Esa especialidad no existe en la clínica.")

def eliminar_especialidad():
    especialidad = input("Ingrese la especialidad a eliminar: ").strip()
    if especialidad in especialidades:
        i = especialidades.index(especialidad)
        especialidades.pop(i)
        cupos.pop(i)
        print(f"Especialidad '{especialidad}' eliminada.")
    else:
        print("Esa especialidad no existe en la clínica.")

def reservar_turno():
    especialidad = input("¿En qué especialidad querés reservar turno? ").strip()
    if especialidad in especialidades:
        i = especialidades.index(especialidad)
        if cupos[i] > 0:
            cupos[i] -= 1
            print(f"Turno reservado en '{especialidad}'. Quedan {cupos[i]} cupos disponibles.")
        else:
            print(f"Lo sentimos, no hay cupos disponibles en '{especialidad}'.")
    else:
        print("Esa especialidad no está disponible en la clínica.")

def cancelar_turno():
    especialidad = input("¿En qué especialidad deseas cancelar el turno? ").strip()
    if especialidad in especialidades:
        i = especialidades.index(especialidad)
        cupos[i] += 1
        print(f"Turno cancelado en '{especialidad}'. Quedan {cupos[i]} cupos disponibles.")
    else:
        print("Esa especialidad no existe en la clínica.")

def ver_especialidades_sin_cupo():
    print("Especialidades sin cupos disponibles:")
    sin_cupo = False
    for i in range(len(especialidades)):
        if cupos[i] == 0:
            print(f"- {especialidades[i]}")
            sin_cupo = True
    if not sin_cupo:
        print("Todas las especialidades tienen cupos disponibles.")

"""MENU de Clinica"""
def menu():
    while True:
        print("\n--- MENÚ DE LA CLÍNICA ---")
        print("1. Agregar especialidad")
        print("2. Consultar cupos")
        print("3. Ver especialidades")
        print("4. Agregar cupos")
        print("5. Eliminar especialidad")
        print("6. Reservar turno")
        print("7. Cancelar turno")
        print("8. Ver especialidad sin cupo")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_especialidad()
        elif opcion == "2":
            consultar_cupos()
        elif opcion == "3":
            ver_especialidades()
        elif opcion == "4":
            agregar_cupos()
        elif opcion == "5":
            eliminar_especialidad()
        elif opcion == "6":
            reservar_turno()
        elif opcion == "7":
            cancelar_turno()
        elif opcion == "8":
            ver_especialidades_sin_cupo()
        elif opcion == "9":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu()