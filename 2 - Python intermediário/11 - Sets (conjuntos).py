"""
Utilizando - Sets

Um set é criado como a mesma chave do dicionário --> '{}'

add (adiciona), update (atualiza), clear, discard
union | (une)
intersection & (todos os elementos presentes no dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)
"""

s2 = {1,2,3,4,5}

s1 = set()
s1.add('Ruan')
s1.add((1,5,7,'Mario'))
s1.add(2)
s1.add(4)
print(s1)
s1.discard(2) # descartando elementos de um set
print("S1 =", s1)

# Diferente de add a funcao update itera os elementos e adiciona Ex:
s3 = set()
s3.update('Python') # A função update faz um incremento (Pega cada letra da palavra python e coloca em uma posição)
print("S3 =", s3)

# um set não aceita elementos duplicados Ex:
s4 = set()

s4.update([1,2,3,4,5,5], {5,6,7,8,9,10})
print("S4 =", s4)

# Um set pode servir para remover elementos duplicados de uma lista Ex:
lista = [1,2,2,2,3,3,4,5,6,'Ruan','Ruan',20]

lista = set(lista)
print(lista)
# {1, 2, 3, 4, 5, 6, 20, 'Ruan'}


# Unindo sets - Maneiras possíveis:

s1 = {1,2,3,4,5}
s2 = {1,2,3,4,5,6}
s3 = s1 | s2 # usando um cast
print("S3 =",s3)

s1 = {1,2,3,4,5}
s2 = {1,2,3,4,5,6}
s3 = s1.union(s2) # Usando um union
print(s3)

s1 = {1,2,3,4,5}
s2 = {1,2,3,4,5,6}
s3 = s1 & s2 # Usando um intersection - Pega os elementos que estão em ambos
print('\nEm ambos',s3)

s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}
s3 = s1 - s2 # Usando diference - junta apenas o elemento que está só no da esquerda
print('\ndiference',s3)

s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}
s3 = s1 ^ s2 # Usando symetric diferences - Pega os elementos que não estao em ambos
print('\nNão estão em ambos',s3)

# Checando se listas são iguais mesmo com elementos duplicados

lis = ['Ruan','Ruan','Ruan',"Mari",'Mari','Rayanne']
lis2 = ['Rayanne','Rayanne','Rayanne','Ruan','Mari','Ruan']

lis = set(lis)
lis2 = set(lis2)

print(lis == lis2)
# True

lis = ['Ruan','Ruan','Ruan',"Mari",'Mari','Rayanne']
lis2 = ['Rayanne','Rayanne','Rayanne','Ruan','Mari','Ruan']

lis = list(set(lis))
lis2 = list(set(lis2))
print(lis,lis2)

# sem alerar as listas

lis = ['Ruan','Ruan','Ruan',"Mari",'Mari','Rayanne']
lis2 = ['Rayanne','Rayanne','Rayanne','Ruan','Mari','Ruan']

if set(lis) == set(lis2):
    print('As listas são iguais')
else:
    print('As listas não são iguais')