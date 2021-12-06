# Laberinto Terminado

---

El link al repositorio de esta actividad es el siguiente: [Laberinto](https://github.com/mat0ta/laberinto/)

Esta actividad ha sido realizada por [mat0ta](https://github.com/mat0ta/)

---

El código escrito para la actividad sigue el siguiente [diagrama de flujo](https://github.com/mat0ta/laberinto/blob/main/diagrama_laberinto.png):

![Diagrama de Laberinto](https://github.com/mat0ta/laberinto/blob/main/diagrama_laberinto.png)

---

El laberinto se crea empleando la lista de coordenada aportadas para realizar la actividad (variable **muro**). Esta registra la posición del muro que delimita el laberinto. Se crea 1 array con 5 arrays vacías en su interior. Acto seguido, empleando el **muro** se indexan estas arrays y empleando un loop **for** se van colocando las X en los lugares correspondientes. A parte, se colocan en inicio (i) y el final (s):

![Creacion](https://github.com/mat0ta/laberinto/blob/main/creacion.png)

El [código](https://github.com/mat0ta/laberinto/blob/main/laberinto.py) empleado para la actividad está basado en un **while loop** el cual cesará con un **break** en la línea *32* ejecutado por la condición de que se haya alcanzado el fin del laberinto, printeando los movimientos realizados:

![Break](https://github.com/mat0ta/laberinto/blob/main/snapshots/break.png)

El resto del **while loop** emplea la misma estructura. Se mueve de la posición en la que está, registrada en la variable **posicion**, mediante la suma de uno o ambos valores, dependiendo de al movimiento a realizar. Una vez hecho, este comprueba si en esta posición a la que va a avanzar es una pared o no. Si lo es, esta vuelve a la posición en la que estaba y comprueba en siguiente movimiento realizando el mismo proceso; si no es una pared, avanza, guarda su posición, añade un punto en esa posición para que no pueda volver atrás y registra el movimiento en la variable **movimientos** para que esta sea printeada al final de la actividad al alcanzar el fin.

A esto se le suma la animación realizada para representar el avance en el laberinto. Esta consiste en el printeo del laberinto cada vez que este avanza para ver el progreso del mismo. Empleando el módulo **os** se ejecuta el comando *cls* para limpiar la consola e inmediatamente después se printea el nuevo laberinto; dejando 1 segundo entre acción y acción para dar efecto de animación (empleando el módulo **time**): 


![Main While](https://github.com/mat0ta/laberinto/blob/main/snapshots/main_while.png)
