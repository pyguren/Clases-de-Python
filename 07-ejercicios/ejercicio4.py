"""
Pedirle 2 numeros al usuario y hacer todas las operaciones 
basicas de una calculadora mostrandolo en pantalla

"""


numero1 = int(input("Dime el primer numero del 1 al 10: "))
numero2 = int(input("Dime el segundo numero del 1 al 10: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f"El resultado de la suma es: {suma}")
print(f"El resultado de la resta es: {resta}")
print(f"El resultado de la multiplicacion es: {multiplicacion}")
print(f"El resultado de la division es: {division}")
