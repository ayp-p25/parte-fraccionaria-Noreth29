"""
Inserta el encabezado aquí y escribe tu código abajo
"""

# Declaraciones
try:
# Entradas
    numero = float(input("Introduzca un número "))

# Proceso
    if numero % 1 == 0:
        print("No tiene decimales")
    else:
        print("Sí tiene decimales")
# Salidas
except ValueError:
    print("Error. Introduzca un número válido.")
