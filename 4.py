#Modificar el ejercicio anterior para leerlo de un archivo.

from io import open
import pathlib, os

ruta = str(pathlib.Path().absolute()) + "/histograma.txt"
os.remove(ruta)
archivo = open (ruta, "a+")

lista = []
try:
    for i in range (0,5):
        num = int(input("ingrese un numero positivo: "))
        lista.append(num)
        #print (lista)
except:
    print("Debe intrducir un numero mayor o igual a cero")

archivo.write("Histograma de 5 elementos \n")
for i in lista:
    archivo.write("*"*i + "\n")
    #print(ast*i)

archivo.close()