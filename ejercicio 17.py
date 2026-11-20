# Nombre: Paloma Collado Mora
# Curso: 2º Bachillerato B
# Ejercicio 17:
# Enunciado Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El
# tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un
# algoritmo que determine la hora de llegada a la ciudad B




H = int(input("Introduce la hora de salida: "))
M = int(input("Introduce los minutos de salida: "))
S = int(input("Introduce los segundos de salida: "))

T = int(input("Introduce el tiempo de viaje en segundos: "))

hora_salida = H * 3600 + M * 60 + S

hora_llegada = hora_salida + T

horas = (hora_llegada // 3600) % 24
minutos = (hora_llegada % 3600) // 60
segundos = hora_llegada % 60

print("La hora de llegada es:", horas, ":", minutos, ":", segundos)
