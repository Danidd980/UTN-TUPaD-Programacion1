#Convertir cadena a mayúsculas o minúsculas según el usuario
cadena = input("Ingresa una cadena: ")
opcion = input("¿Deseas convertirla a mayúsculas (M) o minúsculas (m)? ")

if opcion == "M":
    print("En mayúsculas:", cadena.upper())
elif opcion == "m":
    print("En minúsculas:", cadena.lower())
else:
    print("Opción no válida.")
