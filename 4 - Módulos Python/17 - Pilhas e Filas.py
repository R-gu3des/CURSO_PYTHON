""" 
Pilhas -> LIFO(Last in First Out)
Filas  -> FIFO(First In First Out)

"""

from collections import deque
import queue
from sys import maxsize

from markupsafe import re

fila = deque()
print(fila)

fila.append("João")
fila.append("Maria")
fila.append("Fernando")
fila.append("Jonatam")
fila.append("Lucia")
fila.append("Matilda")


print("Pessoas na fila:", *fila)
for elemento in fila:
    print(elemento)

print(f"Saiu da fila: {fila.popleft()}")



fila2 = deque(maxlen=5) #maxlen decide o tamanho da fila
fila2.extend(["Ruan", "Marta", "Carla", "Jana", "Ademir"]) # A funcao extended permite adicionar varios elementos de uma vez a fila

# Ao adicionar mais um elememento a lista quando já esta no limite, o primeiro elemento da fila sai e o último adicionado entra no final
print(*fila2)

fila2.append("Pamela")
print(*fila2)


# TESTANDO FILA COM LIMITE NA PRÁTICA
from time import sleep


fila3 = deque(maxlen=15)

for x in range(100):
    print(*fila3)
    fila3.append(x)
    sleep(1)