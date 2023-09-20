diccionario = {
    'nombre' : 'lucas',
    'apellido' : 'dalto',
    'subs' : 1000000
}
#Keys() devuelve las claves (tambien nos sirve para iterar) (Nos devuelve un objeeto dict_item)
#Get() obteniendo un objeto con get, sino encuentra nada el programa continua
#Clear eliminando todo del diccionario
claves = diccionario.get('subs')

#diccionario.clear()

#eliminando un elemento del diccionario
#diccionario.pop('nombre')

#Obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario)