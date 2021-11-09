"""
Expressões lambada
"""

def multiplicar(x,y):
    return x * y

funcao_lambda = lambda x, y: x * y # Essa é uma forma de riar uma variávle de forma direta

print(funcao_lambda(2,5))
print(multiplicar(2,5)) 

# Uma função lambada é interessante nesse modelo
lista_produtos = [
    ['p1', 15],
    ['p2', 13],
    ['p3', 40],
    ['p4', 52],
    ['p5', 7]
]

# A expressao lambda pode fazer ordenar de maneira mais fácil

# Cria uma expressao lambda que retorna o elemento i na posicao 1
print(sorted(lista_produtos, key=lambda i: i[1], reverse=True))