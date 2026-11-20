# Nombre: Paloma Collado Mora
# Curso: 2º Bachillerato B
# Ejercicio 16:
# EnunciadoDos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por
# una distancia d. El que está detrás viaja a una velocidad mayor. Se pide hacer un
# algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas
# velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos)
# alcanzará el vehículo más rápido al otro



d = float(input("Introduce la distancia entre los vehículos (km): "))

v1 = float(input("Introduce la velocidad del vehículo más rápido (km/h): "))
v2 = float(input("Introduce la velocidad del vehículo más lento (km/h): "))

tiempo = (d / (v1 - v2)) * 60

print("El vehículo más rápido alcanzará al otro en", tiempo, "minutos")
