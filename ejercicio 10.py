# Nombre: Paloma Collado Mora
# Curso: 2º Bachillerato B
# Ejercicio 10:
# Enunciado: Un alumno desea saber cuál será su calificación final en la materia de Algoritmos.
# Dicha calificación se compone de los siguientes porcentajes:
#  55% del promedio de sus tres calificaciones parciales.
#  30% de la calificación del examen final.
#  15% de la calificación de un trabajo final.



parcial1 = float(input("Introduce la primera calificación parcial: "))
parcial2 = float(input("Introduce la segunda calificación parcial: "))
parcial3 = float(input("Introduce la tercera calificación parcial: "))

examen_final = float(input("Introduce la calificación del examen final: "))
trabajo_final = float(input("Introduce la calificación del trabajo final: "))

promedio = (parcial1 + parcial2 + parcial3) / 3

nota_final = (promedio * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)

print("El promedio de las calificaciones parciales es:", promedio)
print("La calificación final es:", nota_final)
