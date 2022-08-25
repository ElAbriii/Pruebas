# PRUEBA 02. OPERACIONES MATEMÁTICAS_HIJOO

#IMPORTAR UNA LIBRERÍA O BIBLIOTECA DE FUNCIONES MATEMÁTICAS DE PYTHON
import math


# ENTRADA DE DATOS 
''' Declarar o crear variable '''
número_1 = int(input("Escribe el primer número: "))
número_2 = int(input("Escribe el segundo número: "))


# PROCESOS (OPERACIONES O CÁLCULOS MATEMÁTICOS Y/O LÓGICOS)
suma = número_1 + número_2
resta = número_2 - número_1
multiplicación = número_1 * número_2
división = número_1 / número_2

potencia_1 = número_1 ** número_2
potencia_2 = pow(número_1, número_2)

cubo = pow(número_2, 3)
raíz_cuadrada_1 = math.sqrt(25)
raíz_cuadrada_2 = pow(25, 1/2)
raíz_cúbica = pow(número_1, 1/3)

módulo_residuo = número_1 % número_2


# SALIDA DE DATOS
print("La suma es =", round(suma, 2))
print("La suma es =",suma)
print("La suma es =" + str(suma))
#CONCATENACIÓN (+) Es la unión o cuando juntas dos o más textos)
#CASTEO: Convertir un tipo de datos en otro tipo de datos, por ejemplo: dato númerico a texto
print(f"La suma es = {suma}")
#Interpolación de textos
# F = formatear
print()

#RESTA
print("La resta es =",resta)
print("La resta es =" + str(resta))
print(f"La resta es = {resta}")
print()

#MULTIPLICACIÓN
print("La multiplicación es =",multiplicación)
print("La multiplicación es =" + str(multiplicación))
print(f"La multiplicación es = {multiplicación}")
print()

#DIVISIÓN
print("La división es =",división)
print("La división es =" + str(división))
print(f"La división es = {división}")
print()

#POTECIA
print("La potencia1 de num1 y num2 es =",potencia_1)
print("La potencia2 de num1 y num2 es =",potencia_2)
print()

#CUBO
print("El cubo de núm2 es=",cubo)
print()

#RAÍZ CUADRADA
print("La raíz cuadrada1 es =",raíz_cuadrada_1)
print()
print("La raíz cuadrada2 es =",raíz_cuadrada_2)
print()

#RAÍZ CÚBICA
print("La raíz cúbica de num1  es =",raíz_cúbica)
print()

#MÓDULO O RESIDUOS
print("El módulo o residuo es =",módulo_residuo)
print()