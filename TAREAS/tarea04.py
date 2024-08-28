#TAREA 4
#ZAIRA VALENTINA AVILA LAZCANO

#Considera las siguientes calificaciones:
#calif_1 = 10
#calif_2 = 7
#calif_3 = 4
#Calcula el promedio de las calificaciones considerando que:
#La primera nota vale un 15% del total
#La segunda nota vale un 35% del total
#La tercera nota vale un 50% del total
#La siguiente matriz debe cumplir que el 4to valor de cada fila debe ser igual a la suma de los primeros 3 valores. Crea un código para hacer las correcciones necesarias
#matriz = [ [1, 1, 1, 3], [2, 2, 2, 7], [3, 3, 3, 9], [4, 4, 4, 13] ]

calif_1 = 10
calif_2 = 7
calif_3 = 4

# % de cada calificación
porc_1 = 0.15
porc_2 = 0.35
porc_3 = 0.5

# Cálculo del promedio
promedio_ponderado = calif_1 * porc_1 + calif_2 * porc_2 + calif_3 * porc_3

print("El promedio ponderado es:", promedio_ponderado)

# MATRIZ
matriz = [[1, 1, 1, 3],
          [2, 2, 2, 7],
          [3, 3, 3, 9],
          [4, 4, 4, 13]]


for indice_fila in range(len(matriz)):

    fila_actual = matriz[indice_fila]

    suma = fila_actual[0] + fila_actual[1] + fila_actual[2]

    # Reemplazamos el último elemento de la fila por la suma
    fila_actual[3] = suma

# matriz modificada
print("Matriz corregida:")
for fila in matriz:
    print(fila)
