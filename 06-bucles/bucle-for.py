# FOR

"""
for variable in elemento_iterable (lista, rango, etc)
    bloque de instrucciones

"""

contador = 0
resultado = 0

for contador in range(0, 10):
    print("Voy por el " + str(contador))
    
    #resultado = resultado + contador
    resultado += contador

print(f"El resultado de la suma es: {resultado}")

# Ejemplo tabla de multiplicar

print("\n########## Ejemplo #############")

numero_usuario = int(input("¿Qué número quieres la tabla de multiplicar?"))

if numero_usuario <1:
    numero_usuario = 1
    
print(f"\n#### Tabla de multiplicar del número: {numero_usuario} ####")

for numero_tabla in range(1, 11):
    if numero_usuario >= 11:
        print("Esdta tabla de multiplicar es solo hasta el número 10")
        break
        
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
    
else:
    print("Tabla finalizada")