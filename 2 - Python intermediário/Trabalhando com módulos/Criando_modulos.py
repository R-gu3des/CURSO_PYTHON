# No python ao se criar uma váriavel com letra maisucula seu valor não pode ser alterado
import math
from Dados import *

PI = math.pi



def dobraLista(lis):
    return [x * 2 for x in lis]

def multiplica_lista(lis):
    r = 1
    for val in lis:
        r *= val
    return r


# Se você não quiser que o que está dentro do módulo a ser exportado só seja utilizado no main é so fazer:

if __name__ == "__main__":
    print(PI)
    print(dobraLista(lista))
    print(multiplica_lista(lista))
    print(__name__)