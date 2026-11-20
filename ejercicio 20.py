# Nombre: Paloma Collado Mora
# Curso: 2º Bachillerato B
# Ejercicio 20:
# Enunciado: Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos)
# después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20
# céntimos o 10 céntimos).



monedas2 = int(input("¿Cuántas monedas de 2€ tienes? "))
monedas1 = int(input("¿Cuántas monedas de 1€ tienes? "))
monedas50 = int(input("¿Cuántas monedas de 50 céntimos tienes? "))
monedas20 = int(input("¿Cuántas monedas de 20 céntimos tienes? "))
monedas10 = int(input("¿Cuántas monedas de 10 céntimos tienes? "))
total = (monedas2 * 2) + (monedas1 * 1) + (monedas50 * 0.50) + (monedas20 * 0.20) + (monedas10 * 0.10)
euros = total // 10
centimos = total % 10
print("Tienes", euros, "euros y", centimos, "céntimos")