Matriz = [
[6, 4, 2], 
[5, 10, 3],
[9, 2, 1],
]

columna = 3
numeroMayor = 0

for i in range (columna):
    for j in range (columna):
        if Matriz[i][j] > numeroMayor:
            numeroMayor = Matriz[i][j]
            fila = i
print("La fila con el número mas grande es: ", fila)
