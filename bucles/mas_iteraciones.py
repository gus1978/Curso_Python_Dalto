frutas = ['banana','manzana','ciruela','pera','naranja','granada','durazno']
cadena = 'Hola Dalto'
numeros = [2,5,8,9]

#Evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == 'granada':
        continue
    print(f'Me voy a comer una {fruta}')
    
#Evitar que el bucle siga ejecutandose
for fruta in frutas:
    print(f'Me voy a comer una {fruta}')    
    if fruta == 'pera':
        break
    
    
#Recorrer una cadena de texto
for letra in cadena:
    print(letra)
    
#For en una sola linea de codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)     

