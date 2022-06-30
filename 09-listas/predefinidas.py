from itertools import count


cantantes = ["Julio Iglesias", "Bad Bunny", "Camilo", "Alejandro Sanz"]
numeros = [1, 2, 8, 3, 6, 9, 5]


# Ordenar listas
numeros.sort()
print(numeros)

# agregar elementos
cantantes.append("david bisbal")
cantantes.insert(2, "Carlos Vives")
print(cantantes)

# Eliminar elementos

cantantes.pop(0)
cantantes.remove("Bad Bunny")
print(cantantes)

# dar la vuelta a la lista
print(numeros)
numeros.reverse()
print(numeros)

# Buscar dentro de una lista
print("Camilo" in cantantes)

# Contar elementos

print(len(cantantes))

# Cuantas veces aparece un elemento

print(numeros.count(3))

# Conseguir indice

print(cantantes.index("Camilo"))

# Unir dos listas

cantantes.extend(numeros)
print(cantantes)
