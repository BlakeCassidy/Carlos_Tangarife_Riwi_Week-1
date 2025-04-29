
pesoUsuario = input("¿Cuantos kilos pesas?: -> ")
alturaUsuario = input("Ingrese su altura en metros: -> ")

pesoUsuario = float(pesoUsuario)
alturaUsuario = float(alturaUsuario)

imc = pesoUsuario / (alturaUsuario ** 2)

match imc:
    
    case imc if imc < 18.5:
        print("Bajo peso")
    case imc if 18.5 <= imc <= 24.9:
        print("Normal")
    case imc if 25 <= imc <= 29.9:
        print("Sobrepeso")
    case imc if imc >= 30:
        print("Obesidad")
