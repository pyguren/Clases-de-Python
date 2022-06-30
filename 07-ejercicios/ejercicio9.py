"""
Haz un programa que pida al usuario infinitamente hasta llegar al numero 111

"""

contador = 1

while contador < 100:
    numero = int(input("Introduce un numero: "))

    if numero == 111:
        break
    else:
        print(f"Haz introducido el numero {numero}")
