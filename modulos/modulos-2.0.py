#Si el modulo estuviera dentro de una carpeta en la misma ruta
#import funciones_buenas.saludar as m_saludar


import sys


sys.path.append("C:\Users\admin\Desktop\Curso_Python_Dalton\funciones_buenas")

import saludar as modulo_saludo

print(modulo_saludo.saludar("Gustavo"))