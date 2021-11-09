"""
Split, join e enumerate
* split - Divide uma string / Forma uma lista ou atrabiu os outros valores a outras variaveis.
* join - Junta uma lista #str.
* Enumerate - Enumera eleementos de uma lista.
"""

# Criando uma lista com o split

frase = 'Eu sou programador, gosto bastane de python'
lista = frase.split(' ')
lista2 = frase.split(',') # Você que escolhe qual acaractere que vai dividir a string

print(lista)
print(lista2)

# Já a função join destransforma uma lista e transforma em uma string

string = " ".join(lista)
print(string)

# Usando enumerate:
lista3 = ['Ruan','Rayanne',"Maria",'Jonas']

for index, valor in enumerate(lista3):
    print(f'{index + 1}. {valor}')

# Também pode ser feito assim

for ind, val in enumerate(len(lista3), 50): # No caso você pode escolher qual numero sera escolhido para enumerar inicialmente
    print(ind, val)