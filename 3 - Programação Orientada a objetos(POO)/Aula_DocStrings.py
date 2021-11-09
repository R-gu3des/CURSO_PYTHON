"""Essa forma de deixar uma informação sobre o que está senod usado na pasta docString.


Ao quebrar a linha desta forma, o que está a cima fica como nomeação do móulo/pasta/arquivo e tudo 
a baico fica como descrição.
Também é possível passar links e entre outras utilidades(é possívle ver todas na documentação)

fasohnfopankf afal,fál afamdqpomwf qfoqifnkanfpaknmfq
qdqfmqpfnqpfnwoinf qofqpowmfd-wqkd q,d´qpwdll =ql-wdwq=mdq=wkfr]qwçfd qdnqw´dkwqd.w[lq dpomqwd[ pedqomd
qd´qpdkq´pdkq[d,q[w.f~;=çgr~.gdtrhomftiobmpftghktrpohtrh.sd´vkw ]] dqwdwe,d´wepdf.ewdqdiwqdoiqwdl,ofwkwq
qp´qokmdq dqdniuwdq dpoqwdçw dqodw dpoqd qdwndpqd,´qwd qdo,qdwqdwqp´ldç.fqpwomd qdqndq´p,dwidq~çd,w qjndqdw

qdoqdnqdpoqwmdqdw.q´wpdlqwd[ç qdóqwdo]]] qdkmqd9imqd qdimqdwq´çl, qdw,dp 11.5 9+ 6.5 9 26 987 +9 2.6 dqdw
qwdqwdwqd wgeferge ij oijm l ,p ,´pl,. oin iun omp nu nijmn om uy mo, pok uyb uyb pmdqwuidq8uw dqw9ud89uwqd 
qdqwdwqd qdqwhdq8ydb qdwq8udqw8udn dq9duhls,fa´p dqpof,-epfl wqf-we,f-oqdwq d0iwqjdiqwmd f9ewqjf9uwenf dqwudqw.

"""

# Para criar uma váriavel com uma docString Basta usar as aspas desta forma-> """""" | Com isso as apalavras vão ter espaçamentos assim como esta escrito

variavel = """
Desta forma nós conseguimos escrever desta forma:
         e quebrar linha sem 
        sem 
            precisar usar o '\n'

"""

print(variavel)
print(help(16))


# É possível usar um docString em uma função também EX:

def somar(x,y):
    """Soma o primeiro parâmetro com o segundo"""
    
    return x + y

def multiplica(x, y, z):
    """
    multiplica:
    
    Essa função vai ser responsável por multiplicar 
    os parâmetros 'x', 'y', 'z'. 

    :param x: Número 1 
    :type x: inteiro ou float

    :param y: Número 2
    :type y: inteiro ou float

    :param z: Número 3
    :type z: inteiro ou float

    :return: Multiplica x, y e z
    :rtype: retorna um inteiro ou float


    """
    return x * y *z

# Também consguimos usar isso com classes

class MinhaClasse:
    """Essa é uma classe criada apenas como exemplo"""
    print('Hello world')

    def __init__(self):
        """Inicializa os dados"""
        print("Hello world")



"""
Ele não faz nada mas é só um exemplo para você.
Typing - https://docs.python.org/3/library/typing.html
"""

x: int = 10
y: str = "Ruan"
z: bool = False

def funcao(param1: str, param2: float, param3: dict):
    return param1, param2, param3



from typing import List, Union

def funcao2() -> Union [List, dict]: # Essa forma de função permite que você retorne ou ua lista ou um dicionário
    return []
