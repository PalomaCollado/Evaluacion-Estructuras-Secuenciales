# Nombre: Paloma Collado Mora
# Curso: 2º Bachillerato B
# Ejercicio 15:
# Enunciado: Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar
# un algoritmo que intercambie los valores de ambas variables y muestre cuánto valen al final las dos variables.


A = float(input("Introduce el valor de A: "))
B = float(input("Introduce el valor de B: "))

auxiliar = A
A = B
B = auxiliar

print("El valor final de A es:", A)
print("El valor final de B es:", B)
