def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento en el monto total y el porcentaje del descuento.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento
# Llamadas a la función
# Descuento del 10%
monto_total1 = 900
descuento1 = calcular_descuento(monto_total1)
monto_final1 = monto_total1 - descuento1

# Segunda llamada
# descuento (15%)
monto_total2 = 2100
porcentaje_descuento2 = 15
descuento2 = calcular_descuento(monto_total2, porcentaje_descuento2)
monto_final2 = monto_total2 - descuento2

# Resultados
# Descuento del 10%
print(f"Para un monto total de ${monto_total1} descuento del 10%:")
print(f"Descuento: ${descuento1:.2f}")
print(f"Monto final a pagar: ${monto_final1:.2f}\n")
# Descuento del 15%
print(f"Para un monto total de ${monto_total2} descuento del {porcentaje_descuento2}%:")
print(f"Descuento: ${descuento2:.2f}")
print(f"Monto final a pagar: ${monto_final2:.2f}")