"""
¿Cuanto es el X por ciento de X numero

"""


numero1 = int(input("Introduce un numero: "))
numero2 = int(input("¿Que porcentaje quieres obtener?: "))

resultado = (numero1*numero2) / 100
print(f"El {numero2} % de {numero1} es {resultado}")
