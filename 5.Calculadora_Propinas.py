
total_cuenta = float(input("Por favor, ingresa el total de la cuenta: -> $ "))
porcentaje_propina = int(input("¿Qué porcentaje de propina quieres dejar? (10, 15 o 20): "))

calculoPorcentaje = 0

if porcentaje_propina == 10:
  calculoPorcentaje = 0.10
elif porcentaje_propina == 15:
  calculoPorcentaje = 0.15
elif porcentaje_propina == 20:
  calculoPorcentaje = 0.20
else:
  print("Porcentaje de propina no válido. Se calculará con 10%.")
  calculoPorcentaje = 0.10

valor_propina = total_cuenta * calculoPorcentaje
print("El valor de la propina es: -> $ ", valor_propina)