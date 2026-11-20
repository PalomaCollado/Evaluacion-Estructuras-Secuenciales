# Nombre: Paloma Collado Mora
# Curso: 2º Bachillerato B
# Ejercicio 12:
# Enunciado: Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos
# en el plano. Calcula y muestra la distancia entre ellos.

import math

print("Vamos a calcular la distancia entre dos puntos dentro del plano, por lo tanto:")
x1=float(input("Ingrese el primer punto en el eje x: "))
y1=float(input("Ingrese el primer punto en el eje y: "))
x2=float(input("Ingrese el segundo punto en el eje x: "))
y2=float(input("Ingrese el segundo punto en el eje y: "))
distancia=math.sqrt((x2-x1)**2+(y2-y1)**2)
print("La distancia entre los dos puntos es:", distancia)