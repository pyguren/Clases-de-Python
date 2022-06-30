# Bucle While

"""
Estructura de control que itera o repite la ejecución de una serie de instrucciones
tantas veces sea necesario o hasta que deje de cumplirse la condición.

While condition:
    Bloque de instrucciones
    actualización de contador

"""
contador = 1

while contador <= 100:
    print(f"Estoy en el número: {contador}")
    contador = contador + 1
    
print("------------------------------")

contador = 1
muestrame = str(0)

while contador <= 100:
    muestrame = muestrame + "," + str(contador)
    contador += 1
print(muestrame)

print("------------------------------")

print("######Ejemplo##########")


numero_usuario = int(input("¿De que número quieres la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1
    
print(f"\n###Tabla de multiplicar del numero {numero_usuario}")

contador = 1
while contador <= 10:
    print(f"{numero_usuario} x {contador} = {numero_usuario*contador}")
    
    contador += 1
    
else:
    print("Tabla terminada")    