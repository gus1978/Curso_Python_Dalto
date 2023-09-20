numeros = [4,7,42,15]

#Encontrando el numero mayor de una lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#Encontrando el numero menor de una lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

#Redondeando a seis decimales
numero = round(12.345678,2)

#Retorna False -> 0,vacio, False, None / True -> distinto a 0, True, cadena, datos no vacio
resultado_bool = bool(1)


#Retorna True, si todos los valores son verdaderos
resultado_all = all([0,'true',[344,23]])

#Suma todos los valores de un iterable
suma_total = sum(numeros)

print(suma_total)