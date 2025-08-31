# 1) es mayor de edad
# Solicita la edad del usuario
edad = int(input("Por favor, ingresa tu edad: "))


# Verifica si es mayor de edad
if edad > 18:
    print("Es mayor de edad")


# 2) solicita la nota del usuario y muestra si está aprobado o desaprobado según si la nota es mayor o igual a 6:
# Solicita la nota al usuario
nota = float(input("Ingresa tu nota: "))


# Verifica si la nota es mayor o igual a 6
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# 3) programa que permite ingresar un número y verifica si es par usando el operador módulo (%)
# Solicita un número al usuario
num = int(input("Ingrese un número: "))

# Verifica si es par usando el operador módulo (%)
if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


# 4) solicita la edad del usuario y muestra la categoría correspondiente según el rango de edad:
# Solicita la edad al usuario
edad = int(input("Por favor, ingresa tu edad: "))

# Determina la categoría según la edad
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")


# 5)Validación de Contraseña
# Solicita la contraseña al usuario
contrasena = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")

# Verifica la longitud usando len()
if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# 6)Análisis de Sesgo con statistics
import random
from statistics import mean, median, mode

# Genera una lista con 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

# Calcula los valores estadísticos
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)


# Muestra los valores
print(f"Números: {numeros_aleatorios}")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

# Determina el tipo de sesgo
if media > mediana > moda:
    print("Distribución con sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Distribución con sesgo negativo (a la izquierda)")
elif media == mediana == moda:
    print("Distribución sin sesgo")
else:
    print("No se puede determinar claramente un sesgo")



# 7)Verificar si termina en vocal y añadir signo de exclamación
# Solicita una frase o palabra
texto = input("Ingresa una frase o palabra: ")

# Verifica si termina con una vocal (minúscula o mayúscula)
if texto[-1].lower() in "aeiou":
    texto += "!"

# Imprime el resultado
print("Resultado:", texto)



# 8)Transformar el nombre según la opción del usuario
# Solicita el nombre
nombre = input("Ingresa tu nombre: ")

# Solicita la opción de transformación
print("Elige una opción:")
print("1 - Convertir a MAYÚSCULAS")
print("2 - Convertir a minúsculas")
print("3 - Primera letra en mayúscula")
opcion = input("Ingresa 1, 2 o 3: ")

# Aplica la transformación según la opción
if opcion == "1":
    print("Resultado:", nombre.upper())
elif opcion == "2":
    print("Resultado:", nombre.lower())
elif opcion == "3":
    print("Resultado:", nombre.title())
else:
    print("Opción inválida.")



# 9)Clasificación de terremotos por magnitud (escala de Richter)
# Solicita la magnitud del terremoto
magnitud = float(input("Ingresa la magnitud del terremoto: "))


# Clasifica la magnitud según la escala de Richter
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
# Solicita los datos al usuario
hemisferio = input("¿En qué hemisferio estás? (N/S): ").strip().upper()
mes = int(input("Ingresa el número del mes (1-12): "))
dia = int(input("Ingresa el día del mes: "))

# Verifica entrada válida
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
