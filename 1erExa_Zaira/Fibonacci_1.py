# 1. La serie de Fibonacci se define con la siguiente regla de recurrencia:
#
# $F(n) = F(n-1) + F(n-2)$
# donde $n\in\mathbb{N}$ es el $n$-ésimo término de la serie de Fibonacci y los primeros términos son: $F(1) = 1$ y $F(2) = 1$.
#
# - Crear una función que reciba un entero $n$ y devuelva el $n$-ésimo término de la serie de Fibonacci.
# - Recibir por teclado un número $n$ y devuelva el $n$-ésimo término de la serie de Fibonacci.

# ESCRIBE TU CÓDIGO AQUÍ

def ser_fibona (n):
# nombre_funcion->ser_fibona (serie de fibonacci)
# n -> la ocupo para saber al final la n-esima posicion

  if n <= 0: #n (int) es el que yo voy a ingresar;  n menor igual a 0
    return 0 #lo que me devuelve
  else:
    a, b = 0, 1 #ahora bien si n es mayor que 0 se retoman dos var
    #a->0 1er term
    #b->1 2doter
    for n in range(2, n+1): #iterando inicio de bucle
      a, b = b, a+b
    return b #fin bucle-> contiene el valor de la n-esima posicion

n = int(input("Hola soy Zaira, te solicitare que me indiques un valor para n: ")) # Reciba un entero


devuelve = ser_fibona(n)
print("Calculando para", n, "en la sucesión de Fibonacci la posicion n-esima es:", devuelve) # Devuelva el n-ésimo término de la serie de Fibonacci

#FIRMA: ZAIRA VALENTINA AVILA LAZCANO- 9/SEP/2024