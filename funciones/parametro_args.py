#Forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])

resultado2 = suma_total([5,3,9,10,20,3])






#Utilizando el operador * como argumento (*ARGS)
def suma(nombre,*numeros):
    return f'{nombre}, la suma de tus numeros es: {sum(numeros)}'
    
resultado = suma('Lucas',4,5,6,7,9,9)
print(resultado2)    