'''Modificar el programa anterior, ingresando un segundo nro (m) por argumento, que será el encargado de
 indicar cuantas sumas se harán.
  Por ejemplo si ingreso 4 y 5  el resultado será 4 + 44 + 444 + 4444 + 44444 = 49380
'''
num = int(input("ingrese un numero: "))
m = int(input("ingrese otro numero: "))

def sumador(n):
    l = (str(n))
    suma = 0
    resultado = 0
    for i in range(0,m):
        suma += (n*(10**i)) 
        resultado += suma
    print(f"El resultado es {resultado}")

sumador(num)