# 3. A Watson le gusta retar la habilidad matemática de Sherlock. Watson proveerá un valor inicial y un valor final que
# describa el rango de enteros. SherloCK debe determinar el número de cuadrados enteros dentro del rango.
#
# Nota: Un cuadrado entero es un entero cuya raíz es un entero, ej 4, 9, 16.
#
# - Crear una función que reciba dos enteros: $a$ y $b$ y retorne el número d ecuadrados enteros en el rango $[a, b]$

# ESCRIBE TU CÓDIGO AQUÍ

def cuadrados_rango(a, b):
  #considero a y b para la representar super e infer

  c_cuadrados = 0 #  c_cuadrados es a debo contar cuantoss cuadrados perfect llevo encontrados
  i = 1 #i mi var que tiene la func de contar y generar numeros
  cuadrado = 1 #almaceno valor del cuadrado

  while cuadrado <= b: #inicio bucle cuando sea menor o igual de b
    if a <= cuadrado <= b: #si esta dentro del rango a y b
      c_cuadrados += 1
    i += 1 #se incrementa val i y paso al int
    cuadrado = i * i #calcular el cuadrado del val nuevo
  return c_cuadrados, i #val final
a = int(input("El primer paso es que escribas el límite inferior del rango: "))

b = int(input("El segundo psso es que escribas el límite superior del rango: "))

devuelve = cuadrados_rango(a, b)
print("Finalmente , obtenemos que hay", devuelve, "cuadrados perfectos dentro del rango de", a, "a", b)

#FIRMA: ZAIRA VALENTINA AVILA LAZCANO- 9/SEP/2024