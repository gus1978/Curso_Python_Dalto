
#Creando una lista con list()
lista = list((34,55,66,True))

#Devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#Agregando elementos a la lista
lista.append(63)

#Agregando un elemento a la lista en un indice especifico
lista.insert(2,'TOMA PAPA')

#Agregando varios elementos a la lista
lista.extend([False,2030])

#Eliminando un elemento de la lista (por su indice)
lista.pop(3)#-1 para eliminar el ultimo -2 para eliminar el anteultimo y asi sucesivamente

#Removiendo un elemento de la lista por su valor
lista.remove('TOMA PAPA')

#Ordenando la lista ascendente (si usamos el parametro reverse=True lo ordena en reversa)
lista.sort()

#Invirtiendo los elementos de una lista
lista.reverse

#Verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(34)

#eliminando todos los elementos de la lista
#lista.clear()

print(lista)