#Tarea 01-26 de Agosto de 2024
# Zaira Valentina Avila Lazcano
#Realizar las siguientes actividades:
# Crear un script donde impriman un ejemplo de cada uno de los métodos listados en la página:
# https://docs.python.org/3/tutorial/datastructures.html

##list.append(x)
celulas = ["astrocito", "neurona"]
celulas.append("microglia")
print(celulas)

##list.extend(iterable)
cantneuronas = [1, 2, 3]
more_cantneuronas = [4, 5, 6]
cantneuronas.extend(more_cantneuronas)
print(cantneuronas)

##list.insert(i, x)
neurotransmisores = ["dopamina", "serotonina", "glutamato"]
neurotransmisores.insert(1,"gabba")
print(neurotransmisores)

##list.remove(x)
neurotransmisores.remove("gabba")
print(neurotransmisores)

##list.pop([i])
asignar_posicion = [1, 2,3,4,5,6,7]
retirar_item = asignar_posicion.pop(5)
print(asignar_posicion)
print(retirar_item)

##list.clear()
eliminar_lobulos = [1, 2,3,4,5,6,7]
eliminar_lobulos.clear()
print(eliminar_lobulos)

##list.index(x[, start[, end]])
lobulos = ["frontal", "parietal", "occipital", "temporal", "insula", "limbico"]
index = lobulos.index("occipital")
print(index)

##list.count(x)
cerebro_lobulos= [1, 2, 3, 4,4,5,6]
count = cerebro_lobulos.count(4)
print(count)

##list.sort(*, key=None, reverse=False)
neuronas = [3, 1, 4, 2]
neuronas.sort()
print(neuronas)

##list.reverse()
glia = ["astrocitos", "microglía", "oligodendrocitos"]
glia.reverse()
print(glia)

##list.copy()
glia_list = [1, 2,3,4,5,6,7,8,9,10]
glia_list = glia_list.copy()
print(glia_list)


