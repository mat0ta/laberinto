from random import *

laberinto = []

muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))

laberinto.append(([' ']*5))
print(laberinto)

# for i in muro:
#     for i in range(len(muro)):
#         print(i)