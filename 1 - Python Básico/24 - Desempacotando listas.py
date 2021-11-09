"""
Desempacotando listas em python
"""

lista  = ['Rayanne', "Rosângela", 'Fernandes']

# Desempacotamento
n1, n2, n3 = lista # Dessa forma cada valor da lista é atribuido a uma variável

print(n1, n3)

# Para nãao dar erro no desempacotamento por número diferente de elementos

lista2 = ['Ruan', 'Mari', 'Pai', 'Mãe, irmã']
n1, n2, *outra_lista = lista2
print(n1,n2 ,lista2)

lista3 = ['Renato','Lucas','Helena',1,2,3,4,5,6,7,8,9,10]
n1, n2, *listaRestante, ultimoValor = lista3 #Após a variavel com asteristico são pegos os ultimos valores
print(ultimoValor)

