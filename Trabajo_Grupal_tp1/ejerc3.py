#Suma de dígitos de un número de 3 cifras
#Ingresar un número entre 100 y 999.
#Sumar sus dígitos usando módulo (%) y división (//).
# Función para sumar los dígitos
def sumar_digitos(numero):
    digito1 = numero % 10           # Último dígito
    digito2 = (numero // 10) % 10   # Segundo dígito
    digito3 = numero // 100         # Primer dígito
    return digito1 + digito2 + digito3

# Pedir número
numero = int(input("Ingresa un número de 3 dígitos (100 a 999): "))

# Validar que esté en el rango
if 100 <= numero <= 999:
    suma = sumar_digitos(numero)
    print("La suma de los dígitos es:", suma)
else:
    print("Número fuera de rango.")
