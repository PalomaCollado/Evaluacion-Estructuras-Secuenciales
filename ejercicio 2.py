# Nombre: Paloma Collado Mora
# Curso: 2º Bachillerato B
# Ejercicio 2:
# Enunciado:Calcular el perímetro y área de un rectángulo dada su base y su altura.

import math

base = float(input("Introduce la base: "))
altura=float(input("Introduce la altura:"))
perimetro = 2 * (base + altura)
area = base * altura
print("El perímetro es:",perimetro)
print("El área es:", area)
