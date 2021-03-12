# Escriba un programa que acepte una serie de números separados por coma, y genere una lista de python 
# ordenada de manera descendente. ingresando los numeros 5,77,8,33,6,45,38 se debe obtener 
# [77, 45, 38, 33, 8, 6, 5] 

texto = input("Ingrese una serie de numeros separados por una coma: ")
lista = texto.split(",")
#print (lista)
listaNueva = []

for i in lista:
    listaNueva.append(int(i))

#print (listaNueva)
listaNueva.sort(reverse=True)
print (listaNueva)