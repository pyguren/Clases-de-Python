"""
hacer un programa que muestre todos los numeros impares que hay dentro de 2 numeros
que ingrese el usuario

"""

numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el segundo numero: "))

if numero1 < numero2:
    for contador in range(numero1, (numero2 + 1)):
        if contador % 2 == 0:
            print(f"el numero {contador} es par")
        else:
            print(f"el numero {contador} es impar")
else:
    print("El numero 1 debe ser menor al numero 2")
