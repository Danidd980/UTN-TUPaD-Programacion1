#Tamaño de cadena y cantidad de vocales
cadena = input("Ingresa una cadena: ")
tamaño = len(cadena)

# Contar vocales (mayúsculas o minúsculas)
vocales = "aeiouAEIOU"
cantidad_vocales = 0
for letra in cadena:
    if letra in vocales:
        cantidad_vocales += 1

print("Tamaño de la cadena:", tamaño)
print("Cantidad de vocales:", cantidad_vocales)
