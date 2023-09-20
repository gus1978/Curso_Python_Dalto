diccionario = dict(nombre='Lucas',apellidos='Dalto')


#Las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(['Dalto','Rancio']):'jejejej'}


#Creando diccionario con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(['nombre','apellido'])

#Creando diccionario con fromkeys() cambiando el valor por defecto a 'no se'
diccionario = dict.fromkeys(['nombre','apellido'], 'No se')


print(diccionario)