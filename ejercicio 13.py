# Nombre: Paloma Collado Mora
# Curso: 2º Bachillerato B
# Ejercicio 13:
# Enunciado:Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz
# cúbica. Python3 no tiene ninguna función predefinida que permita calcular la raíz
# cúbica, ¿Cómo se puede calcular?

import math

numero=float(input("Ingrese un numero: "))
raiz1=math.sqrt(numero)
raiz2=(numero)**1/3
print("Su raíz cuadrada es ", raiz1, "y su raíz cúbica", raiz2)