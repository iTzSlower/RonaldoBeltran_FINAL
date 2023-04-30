import sys



if len(sys.argv)==3:
        
    frase=sys.argv[1]
    cantidad=int(sys.argv[2])


    for i in range(cantidad):
        print(frase)
else:
    print("che te equivocaste de cantidad de argumentos")