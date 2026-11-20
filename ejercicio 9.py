# Nombre: Paloma Collado Mora
# Curso: 2º Bachillerato B
# Ejercicio 9:
# Enunciado: Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente
# desea saber cuánto deberá pagar finalmente por su compra


compra = float(input("Introduce el importe total de la compra: "))

descuento = compra * 0.15
total_pagar = compra - descuento

print("El descuento aplicado es:", descuento)
print("El importe final a pagar es:", total_pagar)
