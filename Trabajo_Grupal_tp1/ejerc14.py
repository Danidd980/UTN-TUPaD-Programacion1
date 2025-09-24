#¿Existen variables por valor y por referencia en Python?
#En Python, todas las variables son referencias a objetos.
#No existe la distinción clara entre "por valor" y "por referencia" como en Java o C++.
#Pero el comportamiento depende del tipo de dato:
#Tipos inmutables (int, float, str, bool): al "modificarlos", se crea una nueva copia.
#Tipos mutables (listas, diccionarios, objetos personalizados): se pueden modificar directamente.
#ejemplo
# Tipo inmutable (int)
a = 5
b = a
b = b + 1
print("a =", a)  # a sigue siendo 5
print("b =", b)  # b es 6

# Tipo mutable (lista)
lista1 = [1, 2, 3]
lista2 = lista1
lista2.append(4)
print("lista1:", lista1)  # [1, 2, 3, 4]
print("lista2:", lista2)  # [1, 2, 3, 4]
