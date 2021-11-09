"""
Formatando valores com modificadores

:s | Texto (Strings)
:d | Interiros (int)
:f | Números de ponto flutuante (float)
:.(Número)f | Quantidade de casas decimais (float)
:(Caractere)(> ou < ou ^)(Quantidade)(Tipo - s, d, ou f)

> | Direita
< | Esquerda
^ | Centro

"""

# Exemplo de formatação com casas decimais
divisao = 10 / 3
print(10 / 3)
print(f'{1 / 3:.2f}') # Alocando apenas duas casas decimais
print(f'{divisao:.3f}') 


# Fazer com que um elemento tenha um certo número de caracteres
num = 1 
print(f'{num:0>10}') # Aqui diz que O valor terá 10 casas e será preenchido com 0

num2 = 1150
print(f'{num2:0>10}') # terá a mesma quantidade de casas que o ex 1


# Utilizando o valor no centro:
nome = 'Ruan Guedes'
print(f'{nome:=^50}') # A string vai possuir 50 caracteres e será preenchido por '=' nas laterais
# O nome ficará no centro

print(f'{nome:-<50}')
print(f'{nome:->50}')

# Essas funções ainda poderiam ser feitas de outra forma Ex:

print(nome.ljust(20, '#')) # Faz com que a string possua y caracteres e com o que será preenchido lpara left e r para right
print(nome.rjust(20, '#'))
print(nome.center(20,"-"))


nome2 = 'RAYANNE GUEDES'
nome3 = 'rosangela'
print(nome2.lower()) # Deixa os caracteres em minusculo / lower
print(nome3.upper()) # Deixa os caracteres em maiuscuo / Upper

