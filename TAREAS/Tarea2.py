#ZAIRA VALÑENTINA AVILA LAZCANO
#Tarea 2

#Crear un archivo llamado tarea02.py para determinar si los tipos de dato range cumplen:

tupla = ('zai', 'mel', 'clau', 'aneel', 'andy')
print('La tupla:', tupla, 'es de tipo:', type(tupla))


tupla = ('zai', 'mel', 'clau', 'aneel', 'andy')
print('tupla:', tupla)
print('aplicando slicing:', tupla[3])
print('aplicando slicing con números negativos:', tupla[-4: -1])
#mutabilidad
#tupla[3] = tupla('sol')
#print('Tupla mutable', tupla)

#suma
tupla1, tupla2 = ('neuroanato', 'bioquim', 'comneuro', 'gen'), ('tecnicas', 'bioetica', 'mate')
print('suma de tuplas:', tupla1 + tupla2)
print('aplicando la función len:', len(tupla1+tupla2))
print('multiplicando tuplas por un entero:', tupla1*4)
#producto por un entero
#slicing
#convertir a lista o tupla

print('convirtiendo lista a tupla:', tuple(['modelos', 'neuroimagen']),
      'tiene tipo:', type(tuple(['comcel', 'histo'])))

#función len
concatenated_tupla = tupla1 + tupla2
print('Suma de tuplas (concatenation):', concatenated_tupla)
print('aplicando la función len:', len(concatenated_tupla))