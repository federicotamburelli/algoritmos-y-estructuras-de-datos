matriz = [
[0, -4, 2], 
[5, 0, -3],
[0, -2, 0],
]

columnas = 3
positivo = 0

for i in range (columnas):
    for j in range (columnas):
        if matriz [i][j] > 0:
            positivo = positivo + 1


print ("la cantidad de positivos son: ", positivo)
        