# 1) Hola Mundo
print("Hola Mundo!")

# 2) Saludo personalizado
nombre = input("¿Cuál es tu nombre? ")
print(f"Hola {nombre}!")


# 3) Información personal
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


# 4) Área y perímetro de un círculo
import math
radio = float(input("Ingresa el radio del círculo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")


# 5) Segundos a horas
segundos = int(input("Ingresa una cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas:.2f} horas.")


# 6) Tabla de multiplicar
numero_a_multiplicar = int(input("Por favor, ingrese un número entero: "))
print(f"""
  {numero_a_multiplicar} x 0 = {numero_a_multiplicar * 0}
  {numero_a_multiplicar} x 1 = {numero_a_multiplicar * 1}
  {numero_a_multiplicar} x 2 = {numero_a_multiplicar * 2}
  {numero_a_multiplicar} x 3 = {numero_a_multiplicar * 3}
  {numero_a_multiplicar} x 4 = {numero_a_multiplicar * 4}
  {numero_a_multiplicar} x 5 = {numero_a_multiplicar * 5}
  {numero_a_multiplicar} x 6 = {numero_a_multiplicar * 6}
  {numero_a_multiplicar} x 7 = {numero_a_multiplicar * 7}
  {numero_a_multiplicar} x 8 = {numero_a_multiplicar * 8}
  {numero_a_multiplicar} x 9 = {numero_a_multiplicar * 9}
    """)


# 7) Operaciones con dos números
num1 = int(input("Ingresa el primer número (distinto de 0): "))
num2 = int(input("Ingresa el segundo número (distinto de 0): "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")


# 8) Índice de Masa Corporal
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = peso / (altura ** 2)
print(f"Tu índice de masa corporal es: {imc:.2f}")


# 9) Celsius a Fahrenheit
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")


# 10) Promedio de 3 números
num1 = float(input(" Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio es: {promedio:.2f}")
