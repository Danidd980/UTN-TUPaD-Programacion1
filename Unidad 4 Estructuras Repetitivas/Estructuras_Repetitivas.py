#1)imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), forma creciente y número por línea.
for numero in range(0,101):
    print (numero)

#2)solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
numero = input("Ingresa un número entero: ")
print("Cantidad de dígitos:", len(numero.lstrip("-")))
#input() pide el número.
#lstrip("-") elimina el signo negativo si existe.
#len() cuenta cuántos dígitos tiene el número.
