numeros = [1,2,3,4,5,6,7,8,9,20,20,22]

#Creando una funcion lambda para multiplicar por dos
multiplicar_por_dos = lambda x : x*2

#Creando funcion comun que diga si es par o no
#def es_par(num):
 #   if (num%2==1):
#        return True

#Usando filter con ua funcion comun
#numeros_pares = filter(es_par,numeros)

#Creando lo mismo que antes pero con LAMBDA
numeros_pares = filter(lambda numero:numero%2 == 0,numeros)
print(list(numeros_pares))

