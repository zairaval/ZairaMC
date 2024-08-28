#ZAIRA VALENTINA AVILA LAZCANO
#Mostrar un ejemplo de cada una de los siguientes métodos de diccionarios
mi_diccionario = {'nombre': 'Zaira', 'edad': 21, 'ciudad': 'EDOMEX'}

#POP
valor_eliminado = mi_diccionario.pop('edad')
print(valor_eliminado)
print(mi_diccionario)

#get
mi_diccionario = {'nombre': 'Zaira', 'edad': 21}
valor = mi_diccionario.get('ciudad', 'Desconocida')
print(valor)

#copy
mi_diccionario = {'nombre': 'Zaira', 'edad': 21}
copia_diccionario = mi_diccionario.copy()
print(copia_diccionario)

#keys
mi_diccionario = {'nombre': 'Zaira', 'edad': 21, 'ciudad': 'EDOMEX'}
claves = mi_diccionario.keys()
print(claves)  # Output: dict_keys(['nombre', 'edad', 'ciudad'])

#items
mi_diccionario = {'nombre': 'Zaira', 'edad': 21, 'ciudad': 'EDOMEX'}
pares_clave_valor = mi_diccionario.items()
print(pares_clave_valor)

#clear
mi_diccionario = {'nombre': 'Zaira', 'edad': 21, 'ciudad': 'EDOMEX'}
mi_diccionario.clear()
print(mi_diccionario)  # Output: {}

#fromkeys
mi_diccionario = {'nombre': 'Zaira', 'edad': 21, 'ciudad': 'EDOMEX'}
claves = ['nombre', 'edad', 'ciudad']
mi_diccionario = dict.fromkeys(claves, 'Desconocido')
print(mi_diccionario)

#popitem
mi_diccionario = {'nombre': 'Zaira', 'edad': 21, 'ciudad': 'EDOMEX'}
par_eliminado = mi_diccionario.popitem()
print(par_eliminado)  # Output: ('ciudad', 'México')
print(mi_diccionario)

#setdefault
mi_diccionario = {'nombre': 'Zaira', 'edad': 21}
valor = mi_diccionario.setdefault('ciudad', 'México')
print(valor)  # Output: México
print(mi_diccionario)

#update
mi_diccionario = {'nombre': 'Zaira', 'edad': 21}
otro_diccionario = {'ciudad': 'EDOMEX', 'trabajo': 'Estudiante de Neurociencias'}

mi_diccionario.update(otro_diccionario)
print(mi_diccionario)

#values
mi_diccionario = {'nombre': 'Zaira', 'edad': 21, 'ciudad': 'EDOMEX'}
valores = mi_diccionario.values()
print(valores)