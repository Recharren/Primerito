#Rescriba un programa que cree un histograma de una lista de enteros ingresados por teclado. 

lista = []
try:
    for i in range (0,5):
        num = int(input("ingrese un numero cero o mayor: "))
        lista.append(num)
        #print (lista)
    for i in lista:
        print("*"*i)
except:
    print("Debe introducir un numero cero o mayor")
