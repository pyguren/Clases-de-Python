"""
Mostrar todas las tablas de multiplicar que hay del 1 al 10

"""


for cabecera in range(1, 11):
    print(
        f"-------------- Tabla de multiplicar de {cabecera} -----------------")
    for contador in range(1, 11):
        resultado = cabecera*contador
        print(f"El resultado de {cabecera} * {contador} = {resultado}")
