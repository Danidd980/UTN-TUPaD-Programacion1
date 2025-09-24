#Mostrar código ASCII de cada letra de una cadena
cadena = "La lluvia en Mendoza es escasa"

ascii_convertido = ""
for letra in cadena:
    ascii_convertido += str(ord(letra)) + " "

print("Códigos ASCII:", ascii_convertido)

