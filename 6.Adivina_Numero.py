
numeroSecreto = 7

intento = int(input("Adivina el numero. Escribe un numero: -> "))

if intento == numeroSecreto:
  print("Adivinaste")
elif intento < numeroSecreto:
  print("Tu número es menor que el número secreto.")
else:
  print("Tu número es mayor que el número secreto.")