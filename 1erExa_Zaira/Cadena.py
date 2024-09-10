
# 4. Sea una cadena $s$ de letras en minúscula q se repite infinitamente. Dado un entero $n$, encuentra e
# imprime el número de letras 'a' en las primeras $n$ letras de la cadena infinita.
#
# - Crear una función que reciba la cadena $s$ y el entero $n$ y retorne el número de 'a's en las primeras $n$ letras de
# la cadena infinita.
# - Recibir por teclado la cadena $s$ y el entero $n$.

# ESCRIBE TU CÓDIGO AQUÍ

def cont_a(s, n):
    #func->cont_a : s-> string & n-> cant_letras en cadena
    tam_s = len(s) # Calcular tamaño de la cadena s guardar en tam_s
    rep_t= n // tam_s # para saber cuanto cabe en la cadena 's' en las primeras letras
    resto = n % tam_s #de la div anterior


    cont_t = s.count('a') * rep_t # cantidad total de 'a' en las partes repetidas de la cadena

    cont_t += s[:resto].count('a') #Suma al contador anterior

    return cont_t #devuelve el valor final del contador,


# en la cadena y el número de letras
s = input("Escribe la cadena por ejemplo 'abcabc': ")
n = int(input("Agrega el número de letras por ejemplo '10': "))

# para calcular e imprimir
resultado = cont_a(s, n)
print("Aqui tenemos que ", resultado, "letras 'a' en las primeras", n, "letras.")

#FIRMA: ZAIRA VALENTINA AVILA LAZCANO- 9/SEP/2024