"""
Trocando valores das variaveis entre si
"""

x = 10 
y = 'Ruan'
z = 'Mandrake'


x,y = y,x

print(x,y)

x = 10 
y = 'Ruan'
z = 'Mandrake'

x, y, z = z, x, y
print(x, y, z)