archivo = open("archivos\\texto_de_dalto.txt",encoding="utf-8")


'''Leer archivo completo
archivo = archivo_sin_leer.read()'''

#Leer linea por linea
#lineas = archivo_sin_leer.readlines()

#Leer una sola linea
linea = archivo.readline()

#Cerrar el archivo
#archivo.close()


print(linea)