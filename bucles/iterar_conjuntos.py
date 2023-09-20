animales = {'Gato','Perro','Loro','Cocodrilo'}
numeros = {52,16,14,72}



for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}')
    
#recorriendo la conjunto numeros y multiplicanto casa valor por 10    
for numero in numeros:
    resultado = numero * 10
    print(resultado)    

#Iterando dos conjunto del mismo tamaño al mismo tiempo    
for numero,animal in zip(animales,numeros):
    print(f'recorriendo conjunto 1: {numero}')
    print(f'recorriendo conjunto 2: {animal}')

   
    
#Forma correcta de recorrer una conjunto con su indice    
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'El indice es: {indice} y  El valor es: {valor}')
    
#Usando el for/else
for numero in numeros:
    print(f'ejecutando el ultimo bucle, valor actual: {numero}')
else:
    print('El bucle termino')
    
#Funciona correctamente para tuplas y conjuntos