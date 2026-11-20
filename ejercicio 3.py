# Nombre: Paloma Collado Mora
# Curso: 2º Bachillerato B
# Ejercicio 3:
# Enunciado:Dados los catetos de un triángulo rectángulo, calcular su hipotenusa

import math

catetoB = float(input("Ingrese el cateto b: "))
catetoC = float(input("Ingrese el cateto C: "))

hipotenusa = math.sqrt(catetoB**2+catetoC**2)

print("Dado dicho triángulo de cateto b", catetoB, "y cateto c", catetoC, "obtenemos una hipotenusa de:", hipotenusa)