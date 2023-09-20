diccionario = {
    'nombre': 'lucas',
    'apellido': 'Dalto',
    'subs': 100000
}

#Recorriendo diccionario para obtener las claves
for key in diccionario:
    key 
    print(f'La clave es: {key}')
    
#Recorriendo diccionario con item() para obtener la clave y los valores
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'La clave es: {key} y el Valor es: {value}')    