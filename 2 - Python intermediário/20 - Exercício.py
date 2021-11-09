"""
Exercício - Objetos iteraveis e iteradores
"""

from itertools import count

Lista_a = [ 1, 2, 3, 4, 6]
Lista_b = [4, 5 ,6 , 8, 9, 10, 5]

zipado = zip(Lista_a,Lista_b)
print(zipado)
resultado = [va + vb for va, vb in zipado]

print(resultado)

contador = count()

print(next(contador))
print(next(contador))
print(next(contador))

