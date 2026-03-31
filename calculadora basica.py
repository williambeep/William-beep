# Calculadora básica (suma, resta, multiplicacion, division)

def menu():
    print("Calculadora Basica")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    return int(input("Sellecione una opcion: "))

def sumar(num1,num2,num3,num4):
    print("La suma es: ",num1 + num2 + num3 + num4 )

def restar(num1,num2,num3,num4):
    print("La resta es: ",num1 - num2 - num3 - num4)

def multiplicar(num1,num2,num3,num4):
    print("La multiplicacion es: ",num1 * num2 * num3 * num4)

def dividir(num1,num2,num3,num4):
    if num2 == 0 or num3 == 0 or num4 == 0:
        print("Error: No se puede dividir por cero")
    else:
        print("La division es: ",num1 / num2 / num3 / num4)


def pedirNumero():
    return int(input("Ingrese un numero: "))


opcion = menu()
if opcion == 1:
    sumar(pedirNumero(),pedirNumero(),pedirNumero(),pedirNumero())
elif opcion == 2:
    restar(pedirNumero(),pedirNumero(),pedirNumero(),pedirNumero())
elif opcion == 3:
    multiplicar(pedirNumero(),pedirNumero(),pedirNumero(),pedirNumero())
elif opcion == 4:
    dividir(pedirNumero(),pedirNumero(),pedirNumero(),pedirNumero())
elif opcion == 5:
    print("Gracias por utilizar la calculadora")
else:
    print("Error: Opcion no valida")
