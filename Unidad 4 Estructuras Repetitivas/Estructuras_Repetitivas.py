#1)imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), forma creciente y número por línea.
for numero in range(0,101):
    print (numero)

#2)Contar la cantidad de dígitos de un número
def contar_digitos():
    try:
        num = int(input("Ingresa un número entero: "))
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero.")
        return
    if num == 0:
        print("El número tiene 1 dígito.")
        return
    num = abs(num)
    contador = 0
    while num > 0:
        num //= 10 
        contador += 1
    print(f"El número tiene {contador} dígitos.")
contar_digitos()

#3)Sumar números entre dos valores
def sumar_entre_valores():
    try:
        val1 = int(input("Ingresa el primer valor: "))
        val2 = int(input("Ingresa el segundo valor: "))
    except ValueError:
        print("Entrada no válida. Por favor, ingresa números enteros.")
        return
    if val1 > val2:
        val1, val2 = val2, val1
    suma = 0
    for i in range(val1 + 1, val2):
        suma += i

    print(f"La suma de los números entre {val1} y {val2} es: {suma}")
sumar_entre_valores()

#4)Suma secuencial de números
def suma_secuencial():
    suma_total = 0
    while True:
        try:
            num = int(input("Ingresa un número (0 para terminar): "))
            if num == 0:
                break
            suma_total += num
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

    print(f"La suma total acumulada es: {suma_total}")
suma_secuencial()

import random

#5)Juego de adivinanza
def juego_adivinar_numero():
    numero_secreto = random.randint(0, 9)
    intentos = 0
    print("Adivina un número entre 0 y 9.")

    while True:
        try:
            intento_usuario = int(input("Tu intento: "))
            intentos += 1
            if intento_usuario == numero_secreto:
                print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
                break
            elif intento_usuario < numero_secreto:
                print("El número secreto es más grande. ¡Sigue intentando!")
            else:
                print("El número secreto es más pequeño. ¡Intenta de nuevo!")
        except ValueError:
            print("Entrada no válida. Ingresa un número.")
juego_adivinar_numero()

#6)Imprimir números pares en orden decreciente
def pares_decrecientes():
    print("Números pares entre 100 y 0, en orden decreciente:")
    for i in range(100, -1, -2):
        print(i)
pares_decrecientes()

#7)# Sumar números hasta N
def suma_hasta_n():
    while True:
        try:
            num = int(input("Ingresa un número entero positivo: "))
            if num < 0:
                print("Por favor, ingresa un número positivo.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

    suma = 0
    for i in range(num + 1):
        suma += i
    print(f"La suma de los números de 0 a {num} es: {suma}")
suma_hasta_n()

#8)# Clasificar números
def clasificar_numeros():
    cantidad_numeros = 100
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0

    print(f"Por favor, ingresa {cantidad_numeros} números enteros.")
    for i in range(cantidad_numeros):
        try:
            num = int(input(f"Ingresa el número {i + 1}: "))
            
            if num % 2 == 0:
                pares += 1
            else:
                impares += 1

            if num > 0:
                positivos += 1
            elif num < 0:
                negativos += 1
                
        except ValueError:
            print("Entrada no válida. Ese número será ignorado.")

    print("\n--- Resumen de la clasificación ---")
    print(f"Números pares: {pares}")
    print(f"Números impares: {impares}")
    print(f"Números positivos: {positivos}")
    print(f"Números negativos: {negativos}")
clasificar_numeros()

#9)# Calcular la media de N números
def calcular_media():
    cantidad_numeros = 100  
    suma = 0

    print(f"Por favor, ingresa {cantidad_numeros} números enteros para calcular su media.")
    for i in range(cantidad_numeros):
        try:
            num = int(input(f"Ingresa el número {i + 1}: "))
            suma += num
        except ValueError:
            print("Entrada no válida. Ese número no se incluirá en el cálculo.")

    if cantidad_numeros > 0:
        media = suma / cantidad_numeros
        print(f"La media de los {cantidad_numeros} números es: {media:.2f}")
    else:
        print("No se ingresaron números para calcular la media.")
calcular_media()

#10)# Invertir el orden de los dígitos de un número
def invertir_numero():
    try:
        num = int(input("Ingresa un número entero: "))
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero.")
        return
    num_invertido = 0
    num_abs = abs(num)
    while num_abs > 0:
        digito = num_abs % 10
        num_invertido = (num_invertido * 10) + digito
        num_abs //= 10
    if num < 0:
        num_invertido *= -1

    print(f"El número invertido es: {num_invertido}")
invertir_numero()