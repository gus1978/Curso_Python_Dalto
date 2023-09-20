#importantso un modulo y asignandole el nombre "m_saludar"
#import modulo_saludar as m_saludar

#Desde ese modulo, importamos dos funciones y les cambiamos el nombre
from modulo_saludar import saludar as saludar_normal, saludar_raro as saludar_como_coscu

#Creamos las variables con los saludo
saludo = saludar_normal('Lucas')
saludo_raro = saludar_como_coscu('Fran')

#Mostramos los resultados
print(saludo)
print(saludo_raro)

#Para ver las propiedades y metodos de el manespace
#print(dir(m_saludar))

#accedemos al nombre de este modulo
#print(__name__)