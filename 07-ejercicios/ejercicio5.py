"""
Ejercicio 5. Mostrar un programa que muestre todos los numeros entre los 
dos numeros que ingrese el usuario

"""

numero1 = int(input("Dime el primer numero: "))
numero2 = int(input("Dime el segundo numero: "))

if numero1 < numero2:

    for contador in range(numero1, (numero2 + 1)):
        print(contador)

else:
    print("El numero 1 debe ser menor que el numero 2")
