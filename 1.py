'''Realice un programa al que se le da un nro (n) por argumento y el resultado será n + nn + nn. 
    Por ejemplo si ingreso 9 el resultado será 9 + 99 + 999 = 1107
    '''
num = int(input("ingrese un numero: "))
def sumador(n):
    l = (str(n))
    suma = 0
    resultado = 0
    for i in range(0,3):
        suma += (n*(10**i)) 
        resultado += suma
    print(f"El resultado es {l} + {l+l} + {l+l+l} = {resultado}")

sumador(num)