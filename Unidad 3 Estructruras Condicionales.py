#1) Verificar si es mayor de edad
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

#2)Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6,mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario mostrar
#mensaje “Desaprobado”
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#3)programa que permita ingresar solo números pares
numero = int(input("Ingrese un número par: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#4)programa que solicite al usuario su edad e imprima por pantalla a cuál de las categorías pertenece
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#5)Validación de contraseña (entre 8 y 14 caracteres)
contraseña = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6)Detección de sesgo estadístico (media, mediana, moda)
import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("Números aleatorios:", numeros_aleatorios)
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("Distribución no claramente sesgada")

#7)Agregar signo de exclamación si termina en vocal
frase = input("Ingrese una frase o palabra: ")

if frase[-1].lower() in 'aeiou':
    frase += "!"    
print("Resultado:", frase)

#8)Modificar nombre según opción elegida
nombre = input("Ingrese su nombre: ")

print("Opciones:")
print("1. Mostrar en MAYÚSCULAS")
print("2. Mostrar en minúsculas")
print("3. Mostrar con la Primera Letra en mayúscula")

opcion = input("Ingrese el número de la opción deseada (1, 2 o 3): ")

if opcion == "1":
    print("Resultado:", nombre.upper())
elif opcion == "2":
    print("Resultado:", nombre.lower())
elif opcion == "3":
    print("Resultado:", nombre.title())
else:
    print("Opción no válida")

#9)Clasificación de terremotos según la magnitud (Escala de Richter)
magnitud = float(input("Ingrese la magnitud del terremoto: "))

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

#10)Estaciones del año según hemisferio, mes y día
hemisferio = input("¿En qué hemisferio estás? (N/S): ").strip().upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

def obtener_estacion(mes, dia, hemisferio):
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion_norte = "Invierno"
        estacion_sur = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion_norte = "Primavera"
        estacion_sur = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion_norte = "Verano"
        estacion_sur = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion_norte = "Otoño"
        estacion_sur = "Primavera"
    else:
        return "Fecha no válida"

    return estacion_norte if hemisferio == "N" else estacion_sur

estacion = obtener_estacion(mes, dia, hemisferio)
print("La estación actual es:", estacion)