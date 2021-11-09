import time

lista = list(range(10))

print(hasattr(lista,'__iter__')) # Confirmando se a lista possui o método de iteração

# É possivel iterar uma lista utilizando o laço for, mas uma lista não é um iterador

# Maneira de transformar uma lista em um iterador.
# Dessa forma sempre que voçê chamar o next o elemento lista o proximo valor de lista será chamado.
lista = iter(lista)

print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))


####################################################################

"""
Gerador
"""

def gera():
    for n in range(100):
        yield n
        time.sleep(0.05)

g = gera()

for c in g:
    print(c, end=' ')


lista = [x for x in range(100)] # Uma lista
print(type(lista))
lista = (x for x in range(100)) # Um gerador
print(type(lista))

# => Mesmo contendo a mesma expressão: A lista possui um peso na memoria de 9024 bytes, já o gerador possui apenas 88 bytes
# => O mais intrigante é que se ambas as listas fores almentadas de valor, o gerador não almenta sua quantidade de bytes