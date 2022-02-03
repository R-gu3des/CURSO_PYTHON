"""
Threads - São processamentos em paralelo
"""

from os import startfile
from time import sleep
from threading import Thread
from typing import Text

"""
class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.tempo = tempo
        self.texto = texto

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)
    
    

t = MeuThread("Thread 1", 3)
t.start()

t2 = MeuThread("Thread 2", 4)
t2.start()

t3 = MeuThread("Thread 3", 5)
t3.start()

for num in range(15):
    sleep(num)
    print(num)
"""


"""
def printar_algo(texto, tempo):
    sleep(tempo)
    print(texto)

tx = Thread(target=printar_algo, args=("Olá, mundo", 4))
tx.start()

ty = Thread(target=printar_algo, args=("Olá, mundo 2", 5))
ty.start()

tz = Thread(target=printar_algo, args=("Olá, mundo 3", 6))
tz.start()

for c in range(20):
    sleep(0.5)
    print(c)
"""


"""
# Esperando a Thread terminar

def printar_algo(texto, tempo):
    sleep(tempo)
    print(texto)

thread_criada = Thread(target=printar_algo, args=('Olá, mundo!', 10))
thread_criada.start()

while thread_criada.is_alive():
    print('Esperando a Thread terminar!')
    sleep(1)
"""

class Ingresso:
    def __init__(self, estoque):
        self.estoque = estoque

    def comprar(self, quantidade):
        self.lock.acquire() # Forma de não permitir que dê problema de execução na classe se estiver sendo utilizada uma Thread.

        if self.estoque < quantidade:
            print("Quantidade de ingressos insuficiente!")
            self.lock.release()
            return
        else:
            self.estoque -= quantidade
            print(f'Você comprou {quantidade} ingressos!')
            print(f"Quantidade restante {self.estoque}")

        self.lock.release() # Libera para que a classe continue

if __name__ == '__main__':
    ingressos = Ingresso(10)

    threads = []  # Lista para manter as threads
    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        threads.append(t)

    # Inicia as threads
    for t in threads:
        t.start()

    # Verifica se todas as threads terminaram
    executando = True
    while executando:
        executando = False

        for t in threads:
            if t.is_alive():
                executando = True
                break

    print(ingressos.estoque)