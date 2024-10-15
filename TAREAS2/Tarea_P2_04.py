# Ejercicio 1. Mediante teclado especificar los siguiente:
# - Numero de columnas que tendrá el dataframe
# - Una vez que se especifique, preguntar por los datos que tendra esa Serie
# - Preguntar por los nombres de las columnas que tendrá el dataframe
# - Preguntar por los nombres de las filas que tendrá el dataframe
# - Una vez introducidos los datos, crear el dataframe que contenga esa información
# - Mostrar el dataframe

#import pandas as pd

#col_df = int(input ('Ingresa el numero de columnas que tendrá el dataframe: '))

#dat_ser = (input ('Cuales son los datos que tendra esa Serie: '))
#name_colum = []
#for columna in name_colum:
#name_colum =  (input('Cuales son los nombres de las columnas {columna} que tendrá el dataframe: '))

#name_fila =  (input('Cuales son los nombres de las filas que tendrá el dataframe: '))

#data_frame = pd.DataFrame(dat_ser)

#print(data_frame)


import pandas as pd


num_columnas = int(input('Ingresa el número de columnas que tendrá el dataframe: '))


nombres_columnas = []
for i in range(num_columnas):
    nombre = input(f'Ingresa el nombre de la columna {i+1}: ')
    nombres_columnas.append(nombre)


nombres_filas = input('Ingresa los nombres de las filas separados por comas (ej: fila1,fila2): ').split(',')


datos = []
for fila in range(len(nombres_filas)):
    fila_datos = []
    for columna in nombres_columnas:
        valor = input(f'Ingresa el valor para la fila {nombres_filas[fila]} y la columna {columna}: ')
        fila_datos.append(valor)
    datos.append(fila_datos)


df = pd.DataFrame(datos, columns=nombres_columnas, index=nombres_filas)


print(df)
