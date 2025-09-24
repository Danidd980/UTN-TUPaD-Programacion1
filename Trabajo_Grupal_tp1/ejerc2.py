#¿Qué pasa con valores fuera de rango?
#Ver qué ocurre si se asigna un valor demasiado grande a una variable
# Entero muy grande
numero_grande = 10**100  # 1 seguido de 100 ceros
print("Número grande:", numero_grande)

# Float muy grande
numero_float = 1.8e308
print("Número float grande:", numero_float)

# Valor fuera de rango (excede el float)
try:
    numero_fuera_rango = float(1.9e308)
    print("Fuera de rango:", numero_fuera_rango)
except OverflowError as e:
    print("Error de rango:", e)
