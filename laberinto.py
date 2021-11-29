from random import *
import os

laberinto = []

muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))

for i in range(5):
    laberinto.append(([' ']*5))

for i in muro:
    laberinto[int(i[0])][int(i[1])] = 'x'

laberinto[4][4] = 's'

print(laberinto[0])
print(laberinto[1])
print(laberinto[2])
print(laberinto[3])
print(laberinto[4])

# os.system('cls')

posicion = [0, 0]
terminado = False
movimientos = []
i = 0
while not terminado:
    posicion[0] = posicion[0] + 1
    if laberinto[posicion[0]][posicion[1]] == 's':
        print(movimientos)
        break
    if laberinto[posicion[0]][posicion[1]] == ' ':
        laberinto[posicion[0]][posicion[1]] = '.'
        movimientos.append('Abajo')
        i =+ 1
    else:
        posicion[0] = posicion[0] - 1
        posicion[1] = posicion[1] + 1
        if laberinto[posicion[0]][posicion[1]] == ' ':
            laberinto[posicion[0]][posicion[1]] = '.'
            movimientos.append('Derecha')
            i =+ 1
        else:
            posicion[1] = posicion[1] - 1
            posicion[0] = posicion[0] - 1
            if laberinto[posicion[0]][posicion[1]] == ' ':
                laberinto[posicion[0]][posicion[1]] = '.'
                movimientos.append('Arriba')
                i =+ 1
            else:
                posicion[0] = posicion[0] + 1
                posicion[1] = posicion[1] - 1
                if laberinto[posicion[0]][posicion[1]] == ' ':
                    laberinto[posicion[0]][posicion[1]] = '.'
                    movimientos.append('Izquierda')
                    i =+ 1

