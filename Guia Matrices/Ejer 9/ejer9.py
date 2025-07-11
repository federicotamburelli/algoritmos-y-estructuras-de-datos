Matriz = [
[6, 4, 2], 
[5, 10, 3],
[9, 2, 1],
]


po = 0
filas = 3
fila = int(input("escriba el numera de la fila q quiere sumas: "))

for i in range(filas):
    for j in range(filas): 
        if i == fila:
            po = po + 1
            if po == 1:
                num1 = Matriz[i][j]
            if po == 2:
                num2 = Matriz[i][j]
            if po == 3:
                num3 = Matriz[i][j]

suma = num1 + num2 + num3       
 
print("la suma de los numeros de su fila es:", suma)