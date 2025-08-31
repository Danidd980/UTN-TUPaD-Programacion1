# 1) es mayor de edad
edad = int(input("Por favor, ingresa tu edad: "))
if edad > 18:
    print("Es mayor de edad")


# 2) aprobado o desaprobado
nota = float(input("Ingresa tu nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# 3) números pares
num = int(input("Ingrese un número: "))
if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


# 4) categoria por edad
edad = int(input("Por favor, ingresa tu edad: "))
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")


# 5)Validación de Contraseña
contrasena = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")
if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# 6)
import random
from statistics import mean, median, mode
numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print(f"Números: {numeros_aleatorios}")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

if media > mediana > moda:
    print("Distribución con sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Distribución con sesgo negativo (a la izquierda)")
elif media == mediana == moda:
    print("Distribución sin sesgo")
else:
    print("No se puede determinar claramente un sesgo")



# 7)Verificar si termina en vocal y añadir signo de exclamación
texto = input("Ingresa una frase o palabra: ")
if texto[-1].lower() in "aeiou":
    texto += "!"

print("Resultado:", texto)



# 8)Transformar el nombre según la opción del usuario
nombre = input("Ingresa tu nombre: ")

print("Elige una opción:")
print("1 - Convertir a MAYÚSCULAS")
print("2 - Convertir a minúsculas")
print("3 - Primera letra en mayúscula")
opcion = input("Ingresa 1, 2 o 3: ")

if opcion == "1":
    print("Resultado:", nombre.upper())
elif opcion == "2":
    print("Resultado:", nombre.lower())
elif opcion == "3":
    print("Resultado:", nombre.title())
else:
    print("Opción inválida.")



# 9)Clasificación de terremotos por magnitud (escala de Richter)
magnitud = float(input("Ingresa la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")



# 10)Determinar estación según hemisferio, mes y día
hemisferio = input("¿En qué hemisferio estás? (N/S): ").strip().upper()
mes = int(input("Ingresa el número del mes (1-12): "))
dia = int(input("Ingresa el día del mes: "))

if hemisferio not in ["N", "S"] or not (1 <= mes <= 12) or not (1 <= dia <= 31):
    print("Datos inválidos.")
else:
    # Convierte fecha a un número para simplificar comparaciones (mes * 100 + día)
    fecha = mes * 100 + dia

    # Define estaciones por rangos de fechas
    if (fecha >= 1221 or fecha <= 320):
        estacion_norte = "Invierno"
        estacion_sur = "Verano"
    elif 321 <= fecha <= 620:
        estacion_norte = "Primavera"
        estacion_sur = "Otoño"
    elif 621 <= fecha <= 920:
        estacion_norte = "Verano"
        estacion_sur = "Invierno"
    elif 921 <= fecha <= 1220:
        estacion_norte = "Otoño"
        estacion_sur = "Primavera"

    # Muestra la estación correspondiente
    if hemisferio == "N":
        print("Estás en:", estacion_norte)
    else:
        print("Estás en:", estacion_sur)
