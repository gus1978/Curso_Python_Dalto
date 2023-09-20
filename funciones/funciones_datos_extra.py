#Creando una funcion de 3 parametros
#def frase(nombre,apellido,adjetivo):
    #return f'Hola {nombre} {apellido}, sos muy {adjetivo}'

#Utilizando keyword arguments
#frase_resultante = frase('Lucas', 'Dalto', 'Capo')
#print(frase_resultante)

#Creando la misma funcion con un parametro opcional y un valor por defecto
def frase(nombre,apellido,adjetivo = 'Tonto'):
    return f'Hola {nombre} {apellido}, sos muy {adjetivo}'

frase_resultante = frase('Lucas', 'Dalto','Inteligente')
print(frase_resultante)