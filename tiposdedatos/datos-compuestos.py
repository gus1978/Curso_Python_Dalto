#lista se pueden modificar

lista = ['Lucas Dalto', 'Soy Dalto', True, 1.85]

#tupla no se pueden modificar
tupla = (['Lucas Dalto', 'Soy Dalto', True, 1.85])

#esto es valido
lista [3] = 'Maquinola'

#esto no
#tupla (3) = 'Maquinola'


#creando un conjunto (set) no puede haber datos duplicados

conjunto = {'Lucas Dalto', 'Soy Dalto', True, 1.85, 'Soy Dalto'}

#creando un diccionario (dict) (la estructura es key: value y separamos con comas)
diccionario = {
    'nombre' : 'lucas Dalto',
    'canal' : 'Soy Dalto',
    'esta_emocionado' : True,
    'altura': 1.85,
    'dato duplicado' : 'Soy Dalto'
}

print(diccionario['altura'])