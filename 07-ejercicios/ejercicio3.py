"""
Escribir un programa que muestre en pantalla los cuadrados de los primeros 60 numeros 
naturales utilizando el bucle for y luego while

"""
contador = 1

while contador <= 60:
    print(f"El cuadrado de {contador} es ={contador * contador}")

    contador += 1

for contador in range(1, 61):
    print(f"el cuadrado de {contador} es = {contador*contador}")
