"""
Hacer una programa que tenga una lista de 8 numeros enteros y haga lo siguiente:
- Recorrer y mostrar la lista
- Ordenar la lista y mostrarla
- Mostrar su longitud
- Buscar algun elemento que el usuario pida por teclado

"""

# Recorrer y mostrar lista

numeros = [1, 3, 6, 9, 2, 5, 10, 18]

for numero in numeros:
    print(numero)


print("------------------------")

# Ordenar la lista

numeros.sort()
print(numeros)


print("------------------------")

# Mostrar su longitud

print(len(numeros))

print("------------------------")

# Buscar algun elemento que el usuario pida por teclado

busqueda = int(input("Dime un numero: "))

comprobar = isinstance(busqueda, int)

while not comprobar or busqueda <= 0:
    numero_usuario = int(input("Dime un numero: "))
else:
    print(f"Haz introducido el {busqueda}")

print(f"Buscar en la lista el numero {busqueda}")

search = numeros.index(busqueda)
print(f"El numero buscado existe en la lista, es el inice {search}")
