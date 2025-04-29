
año = int(input("Ingresa un año: -> "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
  print(año, "Es un año bisiesto")
else:
  print(año, "No es un año bisiesto")