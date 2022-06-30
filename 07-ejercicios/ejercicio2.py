"""
Ejercicio 2

escribir un script que nos muestre en pantalla todos los numeros pares del 1 al 100

"""

contador = 1

for contador in range(1, 101):
    if contador % 2 == 0:
        print(f"El numero {contador} es par")
    else:
        print(f"El numero {contador} es impar")
