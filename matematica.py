import sys
from funciones_matematicas import sumar, restar, multiplicar, dividir, potencia



if len(sys.argv)==3:
    primernumero= int(sys.argv[1])
    segundonumero= int(sys.argv[2])

    print(f"La suma de {primernumero} y {segundonumero} es {sumar(primernumero,segundonumero)}")
    print(f"La resta de {primernumero} y {segundonumero} es {restar(primernumero,segundonumero)}")
    print(f"La multiplicacion de {primernumero} y {segundonumero} es {multiplicar(primernumero,segundonumero)}")
    print(f"La division de {primernumero} y {segundonumero} es {dividir(primernumero,segundonumero)}")
    print(f"La potencia de {primernumero} y {segundonumero} es {potencia(primernumero,segundonumero)}")

else:
    print("che te equivocaste de cantidad de argumentos")