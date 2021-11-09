"""
A maior diferença entre tupla e lista é que o valor da tupla é imutável
"""

tupla1 = (1,2,3,'Ruan','Guedes','Vieira')# Maneira de instânciar ma tupla 
print(tupla1[::-1])

tupla2 = 1
print(type(tupla2))

tupla2 = 1,
print(type(tupla2)) #Para transformar em uma tupla basta adicionar uma virgula

# Por padrão se voce passar uma variavel com vários valores ela se torna uma tupla

t3 = 1, 2, 3, 456
t4 = 6, 7, 8, 9
t5 = t3 + t4
print(type(t4), t5)

# Passando valores da tupla
n1, n2, n3, *_, nUltimo = t5
print(n1,n2,n3,nUltimo)

# Provando que tupla não pode ser modificada

# t5[2] = 20 
#     t5[2] = 20
# TypeError: 'tuple' object does not support item assignment

# Para mudar o valor basta você alterar a tupla para uma lista e depois convertela novamente

print(t5)
t5 = list(t5)
t5[2] = 200
t5 = tuple(t5)
print(t5)