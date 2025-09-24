#Cajera: Descomponer una cantidad de dinero en billetes y monedas
#Dado un monto, indicar cuántos billetes y monedas se necesitan.
def descomponer_dinero(monto):
    # Billetes y monedas disponibles
    billetes = [200, 100, 50, 20, 10, 5, 2, 1]
    monedas = [0.50, 0.25, 0.10, 0.05]

    print("Desglose de", monto, "en billetes y monedas:")

    # Parte entera
    parte_entera = int(monto)

    # Parte decimal (redondeada a centavos)
    parte_decimal = round((monto - parte_entera) * 100)

    # Billetes
    for billete in billetes:
        cantidad = parte_entera // billete
        parte_entera = parte_entera % billete
        if cantidad > 0:
            print(f"{cantidad} billete(s) de {billete}")

    # Monedas
    for moneda in monedas:
        centavos = int(moneda * 100)
        cantidad = parte_decimal // centavos
        parte_decimal = parte_decimal % centavos
        if cantidad > 0:
            print(f"{cantidad} moneda(s) de {moneda:.2f}")

# Ingreso del monto
monto = float(input("Ingresa una cantidad de dinero (ej. 1390.55): "))
descomponer_dinero(monto)
