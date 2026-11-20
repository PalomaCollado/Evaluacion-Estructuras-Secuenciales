# Nombre: Paloma Collado Mora
# Curso: 2º Bachillerato B
# Ejercicio 19:
# Enunciado: Escribir un algoritmo para calcular la nota final de un estudiante, considerando
# que: por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas
# en blanco 0. Imprime el resultado obtenido por el estudiante.



correcta= int(input("¿Cuántas respuestas correctas has tenido?"))
incorrecta= int(input("¿Cuántas respuestas incorrectas has tenido?"))
blanco= int(input("¿y en blanco?"))
puntos = (correcta*5) - incorrecta
nota = puntos/5
print("Tu nota final es: ",nota)