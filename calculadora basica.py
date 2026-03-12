# calculadora basica (suma, resta, multiplicacion, division) 

num1 = int(input("Ingrese el primer numero: ")) #pide que el usuario ingrese un numero real
num2 = int(input("Ingrese el segundo numero: "))      #pide que el usuario ingrese otro numero real
num3 = int(input("Ingrese el tercer numero: "))   #pide que el usuario ingrese un tercer numero real
num4 = int(input("Ingrese el cuarto numero: "))   #pide que el usuario ingrese un cuarto numero real

operacion = input("Ingrese la operacion (+,-,/,*): ")  #pide al usuario que ingresa que operacion realizar 

if operacion == "+":        # si el usuario ingresa el simbolo de suma, se realiza la suma de los 4 numeros ingresados
    resultado = num1 + num2 + num3 + num4   # imprimira el resultado 
    
elif operacion == "-":    # sino el usuario ingresara el simbolo de resta, se realiza la resta de los 4 numeros ingresados
    resultado = num1 - num2 - num3 - num4

elif operacion == "*":      # sino el usu
    resultado = num1 * num2 * num3 * num4

elif operacion == "/":
    if num2 != 0 and num3 != 0 and num4 != 0:
        resultado = num1 / num2 / num3 / num4
    else:
        resultado = "Error: No se puede dividir por 0"

else:
    resultado = "Operacion no valida"

print("El resultado es: ", resultado)