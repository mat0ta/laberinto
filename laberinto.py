from random import *

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