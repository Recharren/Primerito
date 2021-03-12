#Describa como funciona el programa siguiente:

def fibo(n,a=0,b=1): 
   while n!=0:
      return fibo(n-1,b,a+b)
   return a

for i in range(0,10): #para un valor de i dentro del rango 0 a 10
   print(fibo(i))     # imprimir el retorno de la funcion "fibo" con "i" como argumento

''' el bucle for itera con la variable 'i' en un rango de 0 a 9, luego se imprime el retorno de la 
funcion fibo enviando como argumento 'i'. 
La funcion 'fibo' tiene como argumentos a 'n', 'a' y 'b', estos dos ultimos con un valor por defecto. 
Mientras 'n' sea distinto de cero se retorna 'a', en la proxima iteracion del bucle for 'i' valdra 1, 
entonces se entra al bucle While de 'fibo', en este se retorna la misma funcion pero como argumentos 
tendremos que n=0,a=1,b=1, por ende con n=0 se retorna 'a'. 
En la siguiente iteracion i=2 por ende n=2, entra al bucle While y se ejecuta 'fibo' pero con n=1,a=1,
b=1, lo que provoca que entre de nuevo al While pero con n=0,a=1,b=2, esto retornara el valor de 'a'.
En la siguiente iteracion i=3 por ende n=3, entra al bucle While y se ejecuta 'fibo' pero con n=2,a=1,
b=1, lo que provoca que entre de nuevo al While pero con n=1,a=1,b=2, nuevamente se entra al While con
n=0,a=2,b=3, esto retornara el valor de 'a'.

El programa ejecuta la serie fibonacci donde cada numero sera el resultado de la suma de sus dos 
antecesores
0
1
1
2
3
5
8
13
21
... '''
