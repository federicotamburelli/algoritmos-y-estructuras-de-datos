Matriz = [
[6, 4, 2], 
[5, 10, 3],
[9, 2, 1],
]

po = 0
columnas = 3
encontrarPosicion = int(input("escriba un numero y encontraremos la posicion de este: "))

for i in range (columnas):
    for j in range(columnas): 
        po = po + 1
        if Matriz[i][j] == encontrarPosicion:
            posicion = [i],[j]
            print("tu numero se encuentra en la posicion: ", posicion) 
            break

        
        elif po == 9:
            print("tu numero no esta en la matriz")
        


