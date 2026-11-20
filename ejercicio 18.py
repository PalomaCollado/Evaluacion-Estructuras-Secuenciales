# Nombre: Paloma Collado Mora
# Curso: 2º Bachillerato B
# Ejercicio 18:
# Enunciado Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.


nombre = input("¿Cuál es tu nombre completo? ")
palabras = nombre.split()
print(palabras[0][0], palabras[1][0], palabras[2][0])
