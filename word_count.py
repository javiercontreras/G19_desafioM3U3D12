import string
archivo = open("lorem_ipsum.txt", "r") 

# Leer todo el contenido del archivo
contenido = archivo.read()
archivo.close()
palabras = contenido.split()
print(palabras)
# palabras = contenido.split("\n")
# palabras_s = "".join(palabras)
# print(palabras)
# print(palabras_s)

#Crear un diccionario con todos los characteres en el texto
dict_ch = {ch:ch for ch in contenido}
#Crear un diccionario con todos las palabras
dict_palabras = {palabra:palabra for palabra in palabras}
#Contador de claves en diccionario characters
resultado = 0
contador = 0
for values in dict_ch.values():
    resultado += 1

for values in dict_palabras.values():
    contador += 1


print(f"Hay {resultado} caracteres distintos")
print(f"Hay {contador} palabras distintas")
# Cerrar el archivo
archivo.close()

