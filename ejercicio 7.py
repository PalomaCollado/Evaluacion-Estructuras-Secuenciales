# Nombre: Paloma Collado Mora
# Curso: 2º Bachillerato B
# Ejercicio 7:
# Enunciado:Realiza un programa que reciba una cantidad de minutos y muestre por pantalla
# a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas
# y 40 minutos


import math

minutos = float(input("Ingrese la cantidad de minutos: "))

horas = minutos // 60
minutos2 = minutos % 60
print(minutos, "minutos esquivalen a", horas, "horas y", minutos2, "minutos")