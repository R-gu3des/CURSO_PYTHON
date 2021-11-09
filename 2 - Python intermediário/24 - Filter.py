"""
Filter - retorna os valores se uma condição for verdadeira

-> Filter retorna um objeto iteravel

"""
from Dados import lista, produtos, pessoas

new_lista = filter(lambda valores: valores > 5, lista) # Esta expressão esta peruntando se os valores que estão sendo percorridos são maiores do que 5

for numeros in new_lista:
    print(numeros)

print('-+' * 30)

# Usando filter para dicionários:

preco_dicionario = filter(lambda va: va['preco'] > 50,produtos)

for c in preco_dicionario:
    print(c)

print('-+' * 30)

def filtra(produto):
    if produto['preco'] > 70:
        produto['e_caro'] = True
    return True

nova_lista = filter(filtra, produtos) # Tanto no map quanto no filter se passa antes uma função e depois o local(lista, dicionário ...)

for elementos in nova_lista:
    print(elementos)
print('-+' * 30)

def filtra_Maior18(pessoa):
    if pessoa['idade'] > 18:
        return True
    else:
        return False
    

maiores_18 = filter(filtra_Maior18, pessoas)

for c in maiores_18:
    print(c)

