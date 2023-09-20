#le pedimos al usuario que nos diga una frase o varias
frase = input('Decime una frase y te calculo cuanto tardaria si tuvieras que decirla: ')

#Creamos una lista con todos las palabras de la frase (se separan cada vez que haya un espacio en blanco)
palabras_separadas = frase.split(' ')

#usamos len() para ver la cantidad de elementos que hay en la lista
cantidad_de_palabras = len(palabras_separadas)

#En caso de que tarda mas de un minuto en decirlo, le decimos que pare un poco
if cantidad_de_palabras > 120:
    print('Para flaco tampoco es un testamento')
    
#Calculamos cuanto tardaria en deci las palabras y se lo decimos    
print(f' Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlos')
print(f' Dalto lo diria en {cantidad_de_palabras* 100 // 2*1.3 / 100} segundos en decirlo')