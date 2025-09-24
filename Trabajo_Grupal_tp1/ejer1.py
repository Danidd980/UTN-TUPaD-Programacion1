#CASTEO: Conversión de un número decimal a otros tipos
#Pedir un número decimal (float) al usuario.
#Convertir ese número a distintos tipos: int, str, bool.
# Solicitar al usuario un número decimal
valorDecimal = float(input("Ingresa un número decimal: "))

# Casteo a entero (int) — trunca los decimales
valorEntero = int(valorDecimal)

# Casteo a cadena de texto (str)
valorTexto = str(valorDecimal)

# Casteo a booleano (bool) — si es 0.0 será False, si no True
valorBooleano = bool(valorDecimal)

# Mostrar resultados
print("Original (float):", valorDecimal)
print("Como entero (int):", valorEntero)
print("Como texto (str):", valorTexto)
print("Como booleano (bool):", valorBooleano)