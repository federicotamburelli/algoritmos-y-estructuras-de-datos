Matriz = [
[6, 4, 2], 
[5, 10, 3],
[9, 2, 1],
]

filas = 3
fila1 = int(input("ingrese un numero de alguna fila: "))
fila2 = int(input("ingrese un numero de alguna fila: "))
po = 0
pu = 0

num1 = num2 = num3 = 0
nump1 = nump2 = nump3 = 0

for i in range(filas):
    for j in range(filas): 
        if i == fila1:
            po = po + 1
            if po == 1:
                num1 = Matriz[i][j]
            if po == 2:
                num2 = Matriz[i][j]
            if po == 3:
                num3 = Matriz[i][j]

                
            if j == fila2:
                 pu = pu + 1
            if pu == 1:
                nump1 = Matriz[i][j]
            if pu == 2:
                nump2 = Matriz[i][j]
            if pu == 3:
                nump3 = Matriz[i][j]

Matriz[fila1] = [nump1, nump2, nump3]

Matriz[fila2] = [num1, num2, num3]

print(Matriz)