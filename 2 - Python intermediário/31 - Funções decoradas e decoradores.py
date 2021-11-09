def falaOi():
    print('oi')

variavel = falaOi
variavel()
falaOi()

def master():
    def slave():
        print('oi')

# Se a função for criada desta forma ela não irá mostrar nada, apenas criará uma função.
# É precisso chamar a função dentro da função.

def master2():
    def slave():
        print('hello, world!!')
    slave()

master()


def master3(funcao):
    def slave():
        funcao()
    return slave


def falaOla():
    print('olá')

falaOla = master3(falaOla)
falaOla()

from time import sleep

def demora():
    for c in range(5):
        sleep(1)
        print(c)

demora()


from time import time
from time import sleep

def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time)
        print(f"A função {funcao.__name__} levou {tempo:.2f}ms para executar")
        return resultado
    return interna


# Agora vamos decorar a função demora com a função velocidade

@velocidade
def demora():
    for i in range(5):
        print(i)

demora()