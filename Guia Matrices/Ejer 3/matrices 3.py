Matriz = [
[6, 4, 2], 
[5, 10, 3],
[9, 2, 1],
]

columna = 3
numeroMayor = 0

fila = int(input("Ingrese la fila del 0 al 2 "))
for i in range (columna):
    for j in range (columna):
        if i == fila:
            if Matriz[i][j] > numeroMayor:
                numeroMayor = Matriz[i][j]
if fila > 2:
    print("Ingrese un numero correcto: ")
    fila = int(input("Ingrese la fila del 0 al 2 "))
if fila < 0:
    print("Ingrese un numero correcto: ")
    fila = int(input("Ingrese la fila del 0 al 2 "))
    
print("El numero mayor de la fila ", fila, " es: ", numeroMayor)

