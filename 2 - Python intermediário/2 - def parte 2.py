"""
Funções (def) em python - return
"""
def funcao(a):
    a * 2

variavel = funcao(2)

if variavel:
    print(variavel) # Quando uma função não retorna algo ela é dada como 'none/ expressão falsa
else:
    print('Nenhum valor') 



def funcao2(a):
    return a * 2

variavel2 = funcao2(2)

if variavel2:
    print(variavel2)
else:
    print('Nenhum valor') 

# Uma função não executa mais código após o return


# Comportamento estranho
def f(var):
    print(var)

def dumb():
    return f

var = dumb()('Meu valor que vem de f')
print(var)

# Var acaba se tornando uma function, já que ele executa f
# Ambos estão no mesmo espaço de memória
var = dumb()
if var == f:
    print('Var é igual a f')
else:
    print('Não é')