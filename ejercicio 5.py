# Nombre: Paloma Collado Mora
# Curso: 2º Bachillerato B
# Ejercicio 5:
# Enunciado:Escribir un programa que convierta un valor dado en grados Fahrenheit a grados
# Celsius. Recordar que la fórmula para la conversión es: C = (F-32)*5/9

import math

grados = float(input("Introduce el numero de grados Fahrenheit: "))
celsius = (grados-32)*5/9

print("Tus grados en Celsius han pasado a ser:", celsius)
