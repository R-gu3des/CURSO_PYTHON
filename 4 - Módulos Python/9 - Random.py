"""
O módulo random é utilizado para escolher números de maneira aléatoria e mais
"""

import random

# Inteiro aléatorio entre x,y
int_aleatorio = random.randint(10,20) 
print(int_aleatorio)

# Float aléatorio entre x,y
float_aleatorio = random.uniform(10,20) 
print(float_aleatorio)

# Gera um número de ponto flutuante entre 0 e 1
flutuante = random.random()
print(flutuante)

# Número aleatório usando a função range
aleat_range = random.randrange(1,100, 10)
print("Número aleatório usando a função range:", aleat_range)



lista = ["Janina", "Maria", "Mariana", "Jonatan","Pedro", "Diogo"]

# Escolhe um elemento aleatório da lista
sorteado = random.choice(lista)
print(sorteado)

# Escolhe quantos elementos forem pedidos aletoriamente, podendo haver repetições
sorteados = random.choices(lista, k=2) # 'k' é onde você passa o número de elementos a serem escolhidos
print(sorteados)

# Escolhe quantos elementos forem pedidos aletoriamente, sem haver repetições
sorteadoSemRepeticao = random.sample(lista, 3)
print(sorteadoSemRepeticao)

# Embaralha uma lista
random.shuffle(lista)
print(list(lista))

# Gera uma senha aleatória
import string # Esse módilo retorna o abc em maiscúlo ou minusculo
letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%.&*_-'
geral = letras + digitos + caracteres
senha = ''.join(random.choices(geral, k=15)) # Como o random choices retorna uma lista, usamos a função join para criar uma string
print(senha)
