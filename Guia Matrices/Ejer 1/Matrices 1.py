matriz = [
[0, 4, 2], 
[5, 0, 3],
[0, 2, 0],
]

columnas = 3
suma = 0

for i in range (columnas):
    for j in range (columnas):
        suma += matriz [i] [j]

print ("la suma de los valores de la matriz da: ", suma)