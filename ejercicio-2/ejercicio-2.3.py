#Creando una funcion que muestre la serie fibonacci entre 0 el numero dado

#def fibonacci(num):
    #a,b = 0,1
    #fibonacci_lista = [0]
    #for i in range(num):
        #if b > num: return fibonacci_lista
        #else:
            #fibonacci_lista.append(b)
            #a,b = b,a+b
            
#resultado = fibonacci(34)
#print(resultado)

class ContadorMascotas:
    def __init__(self, mascotas):
        self.mascotas = mascotas

    def contar_mascotas_con_mismo_nombre(self):
        resultado = {}
        
        for nombre, cantidad in self.mascotas.items():
            if nombre in resultado:
                resultado[nombre] += cantidad
            else:
                resultado[nombre] = cantidad
        
        return resultado

# Crear una estructura de datos de ejemplo
mascotas = {
    'William': 5,
    'Floyd': 2,
    'William': 6,
    'Jose': 20,
    'Marcos': 4
}

# Crear una instancia de la clase ContadorMascotas
contador = ContadorMascotas(mascotas)

# Contar las mascotas con el mismo nombre
resultado = contador.contar_mascotas_con_mismo_nombre()

# Mostrar el resultado
print("Resultado:", resultado)







