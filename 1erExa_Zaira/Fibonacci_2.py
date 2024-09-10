
# 2. Utilizando la función del ejercico anterior, recibir por teclado un entero $n$ e imprimir los $n$-ésimos términos de
# la serie de Fibonacci.

# ESCRIBE TU CÓDIGO AQUÍ
def ser_fibona(n):

  if n <= 0: #n menoor o igual a 0
    return [] #lista
  else: #cuando sea mayor n que 1
    seq_fibona = [0, 1]
    for n in range(2, n):
      seq_fibona.append(seq_fibona[-1] + seq_fibona[-2])
    return seq_fibona

n = int(input("Podrias teclear la cant. de números de términos que quieres saber de la sucesión de Fibonacci: "))
#aqui indico lo que quiero que el profe ingrese

devuelve = ser_fibona(n) #devuelve-> almacena el valor n +calculo
print("Para los ", n, "términos en la sucesión de Fibonacci deberian ser:", devuelve)
#imprimir el resultado final almacenado en devuelve

#FIRMA: ZAIRA VALENTINA AVILA LAZCANO- 9/SEP/2024