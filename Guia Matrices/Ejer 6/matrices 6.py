Matriz = [
[6, 4, 2], 
[5, 10, 3],
[9, 2, 1],
]

fila = 3
numeroMayor = 0

for i in range (fila):
    for j in range (fila):
        if Matriz[i][j] > numeroMayor:
            numeroMayor = Matriz[i][j]
            columna = j
print("La fila con el número mas grande es: ", columna)
