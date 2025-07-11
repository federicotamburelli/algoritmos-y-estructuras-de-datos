Matriz = [
[6, 4, 2], 
[5, 10, 3],
[9, 2, 1],
]

fila = 3
numeroMayor = 0

columna = int(input("Ingrese la fila del 0 al 2 "))
for i in range (fila):
    for j in range (fila):
        if i == columna:
            if Matriz[j][i] > numeroMayor:
                numeroMayor = Matriz[j][i]
if columna > 2:
    print("Ingrese un numero correcto: ")
    columna = int(input("Ingrese la fila del 0 al 2 "))
if columna < 0:
    print("Ingrese un numero correcto: ")
    columna = int(input("Ingrese la fila del 0 al 2 "))
    
print("El numero mayor de la columna ", columna, " es: ", numeroMayor)