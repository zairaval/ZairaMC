#TAREA P2 03
#NOMBRE: ZAIRA VALENTINA ÁVILA LAZCANO

import numpy as np
import matplotlib.pyplot as plt

# Ejercicio 1. Genera un arreglo 1D, llamado freq, de 4 elementos de números aleatorios enteros en el intervalo [1, 8]
freq = np.random.randint(1, 9, 4)  # Generamos 4 números aleatorios entre 1 y 8 (inclusivo)

print("Arreglo generado: ", freq)

# Visualización opcional (histograma)
plt.hist(freq, bins=8, range=(0.5, 8.5))
plt.title("Histograma de Frecuencias")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()

# Ejercicio 2. Genera un arreglo 1D, llamado amplitud, de 4 elementos de números aleatorios con distribución uniforme
# en el intervalo [3, 6]
amplitud = np.random.uniform(3, 6, 4)

print("Arreglo de amplitudes:", amplitud)

# Ejercicio 3. Use el metodo arange para generar un arreglo, llamado t, de 2000 números en el intervalo [0, 1]
t = np.arange(0, 1.01, 0.0005)  # 2000 números con un paso de 0.0005

print("Arreglo t:", t)

# Ejercicio 4. Genere 4 ondas sinusoidales con cada frecuencia y amplitud.
# Hint: recuerde que la ecuación de la onda sinusoidal es y(t) = A*sin(2*piB*t) donde A es la amplitud y B es la
# frecuencia. Para usar pi en numpy, use np.pi
# Sugerencia: para visualizar las ondas sinusoidales puede usar las líneas de código
# Parámetros de las ondas
amplitudes = [2, 1.5, 3, 0.8]
frecuencias = [2, 4, 1, 3]

# Generar el vector de tiempo
t = np.linspace(0, 2, 1000)  # Tiempo de 0 a 2 segundos con 1000 puntos

# Crear una figura y un eje
fig, ax = plt.subplots()

# Generar y graficar cada onda
for A, B in zip(amplitudes, frecuencias):
    y = A * np.sin(2 * np.pi * B * t)
    ax.plot(t, y, label=f"Amplitud={A}, Frecuencia={B}")

# Personalizar la gráfica
ax.set_xlabel('Tiempo (s)')
ax.set_ylabel('Amplitud')
ax.set_title('Ondas Sinusoidales')
ax.legend()

plt.show()

# Ejercicio 5. Cree un arreglo llamado x, que sea la suma de las 4 ondas sinusoidales


# Numpy también permite aplicar operadores tales como la transormada de fourier a un arreglo de datos con
# el paquete np.fft, en particular la función np.fft.fft(x) aplica la transformada discreta de fourier al arreglo x
#X = np.fft.fft(x)
# Parámetros de las ondas
amplitudes = [2, 1.5, 3, 0.8]
frecuencias = [2, 4, 1, 3]

# Generar el vector de tiempo
t = np.linspace(0, 2, 1000)  # Tiempo de 0 a 2 segundos con 1000 puntos

# Crear una figura y un eje
fig, ax = plt.subplots(2, 1, figsize=(10, 8))

# Generar y sumar las ondas
x = np.zeros_like(t)  # Inicializamos un arreglo de ceros para almacenar la suma
for A, B in zip(amplitudes, frecuencias):
    y = A * np.sin(2 * np.pi * B * t)
    x += y
    ax[0].plot(t, y, label=f"Amplitud={A}, Frecuencia={B}")

# Graficar la onda resultante
ax[0].plot(t, x, label='Señal resultante', linewidth=2)
ax[0].set_xlabel('Tiempo (s)')
ax[0].set_ylabel('Amplitud')
ax[0].set_title('Suma de Ondas Sinusoidales')
ax[0].legend()

# Aplicar la transformada de Fourier
X = np.fft.fft(x)

# Calcular las frecuencias
freqs = np.fft.fftfreq(len(x), t[1]-t[0])

# Graficar el espectro de frecuencias
ax[1].plot(freqs, np.abs(X))
ax[1].set_xlabel('Frecuencia (Hz)')
ax[1].set_ylabel('Magnitud')
ax[1].set_title('Espectro de Frecuencias')

plt.tight_layout()
plt.show()
# Ejercicio 6. Cree un arreglo, llamado frequence, de los enteros en el intervalo [0, 1999]

frequencies = np.arange(0, 2000)

print(frequencies)

# Ejercicio 7. Calcular el valor absoluto a todos los elementos del arreglo X

# Suponiendo que ya tienes el arreglo X

# Calcular el valor absoluto de todos los elementos de X
X_abs = np.abs(X)

print("Valores absolutos de X:", X_abs)

# Ejercicio 8. De los primeros 10 elementos del arreglo del ejercicio anterior, determine los 4 elementos máximos y en
# qué índices se localizan
# Suponiendo que ya tienes el arreglo X

# Suponiendo que X es un arreglo de al menos 10 elementos
X = np.random.rand(20)  # Ejemplo: Crea un arreglo aleatorio de 20 elementos

# Tomar los primeros 10 elementos
primeros_10 = X[:10]

# Encontrar los índices de los 4 valores máximos
indices_maximos = np.argsort(primeros_10)[-4:]

# Obtener los valores máximos
valores_maximos = primeros_10[indices_maximos]

print("Los 4 valores máximos son:", valores_maximos)
print("Sus índices en los primeros 10 elementos son:", indices_maximos)

# Ejemplo de visualización del espectro de frecuencia (ajusta según tus datos)
frequence = np.arange(100)  # Ejemplo de arreglo de frecuencias
absX = np.random.rand(100)  # Ejemplo de arreglo de magnitudes

plt.stem(frequence, absX)
plt.xlabel('Frecuencia')
plt.ylabel('Magnitud')
plt.title('Espectro de Frecuencias')
plt.show()