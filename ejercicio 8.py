# Nombre: Paloma Collado Mora
# Curso: 2º Bachillerato B
# Ejercicio 8:
# Enunciado:Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas,
# el vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por
# las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en
# cuenta su sueldo base y comisiones.


sueldo_base = float(input("Introduce el sueldo base: "))

venta1 = float(input("Introduce el importe de la primera venta: "))
venta2 = float(input("Introduce el importe de la segunda venta: "))
venta3 = float(input("Introduce el importe de la tercera venta: "))

comision1 = venta1 * 0.10
comision2 = venta2 * 0.10
comision3 = venta3 * 0.10

total_comisiones = comision1 + comision2 + comision3
sueldo_total = sueldo_base + total_comisiones

print("Comisión de la primera venta:", comision1)
print("Comisión de la segunda venta:", comision2)
print("Comisión de la tercera venta:", comision3)
print("Total de comisiones:", total_comisiones)
print("Sueldo total del mes:", sueldo_total)