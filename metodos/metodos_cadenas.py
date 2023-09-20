cadena1 = 'Hola,cojiote,como,estas'
cadena2 = 'Bienvenido perro'

#covierte a mayuscula
mayuscula = cadena1.upper()

#covierte a minuscula
minuscula = cadena1.lower()

#primer letra mayuscula
primer_letra_mayuscula = cadena1.capitalize()

#buscamos una cadena en otra cadena, sino hay coincidencias se vuelve -1
busqueda_find = cadena1.find('H')

#buscamos una cadena en otra cadena, sino hay coincidencias lanza una excepcion
busqueda_index = cadena1.index('H')


#si es numerico devolvemos TRUE, sino devolvemos FALSE
es_numerico = cadena1.isnumeric()

#si es alfanumerico devolvemos true, sino devolvemos false
es_alfanumerico = cadena1.isalpha()

#buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincida 
contar_coincidencias = cadena1.count('o')

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
empieza_con = cadena1.startswith('H')

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
termina_con = cadena1.endswith('te')

#si el valor 1 se encuentra en la cadena original, reemplaza el valor 1 de la misma por el valor 2
cadena_nueva = cadena1.replace('la', 'Mamalo maquina')

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(',')

print ((cadena_separada)[3])



