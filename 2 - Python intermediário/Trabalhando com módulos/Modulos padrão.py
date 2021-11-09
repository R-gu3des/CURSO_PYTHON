# Módulo padrão do python:
# Módulos são arquivos .py (que contém código python) e servem para expandir
# as funcionalidades padrão da linguagem
# veja todos os módulos padrão do python em
# https://docs.python.org/3/py-modindex.html


# Se quisermos importar o módulo inteiro
import sys

print(sys.platform)

# Se quisermos importar uma função específica do módulo

from sys import platform

print(platform)


# Também podemos importar e nomear da maneira que quisermos (Como um apelido) Ex:

from sys import platform as pl # O as serve para passarmos  a nomeação que queremos

print(pl)


from random import randint as randint_orig

for c in range(11):
    print(randint_orig(0,10))

# É necessário tomar cuidado para não sobrescrever um módulo

def randint(*args):
    return 'hahaha'

for c in range(11):
    print(randint(0,10))

# Se você ainda quiser criar uma função com o mesmo nome que o módulo, sê um epelido para a módulo
# Outra maneira seria importar o módulo inteiro

import random # Porém essess métodos so podem ser acessados atrvés do ponto
# Já como o uso do ateristico * ele importa tudo com seu nome

# ex: 

from math import *


from random import randint, random

for v in range(10):
    print(randint(0,10), random())

# Métodos que não vem como padrão em python odem ser instalados 
# pelo terminal com a função 'pip install + "nome do módulo"'
# Para desinstalar o módulo instalado basta digitar o 'pip unistall + "nome do módulo instalado"'

