"""
Dicionarios em python
"""
import copy

# formas de se criar um dicionario
dicionario = {"Ruan" : "10 anos"}
print(dicionario)
dicionario['Altura'] = 1.75
print(dicionario)

# Uma chave não pode aparecer mais de uma vez no dicionario
# Apenas o ultimo valor será implementado. Ex:

dicionario['chave'] = 10
dicionario['chave'] = 20
dicionario['chave'] = 'Valor'

print(dicionario)

############################################################################################

# Chaves e valores podem receber varios tipos de tipo de elementos

d2 = {
    'Qualquer coisa' : 123,
    123 : 'Feijão',
    (1,2,3,4) : 'tupla'
}

print(d2)
print(d2[(1,2,3,4)])

# Maneira de analisar se um dicionario tem a chave existente:
if d2.get('nomedachave') is not None:
    print(f"Utilizando o get do dicionário: {d2.get('nomedachave')}")


# Deletando valores de um dicionário:
del dicionario['Ruan']
print(dicionario)


# É possível acessar os valores e a chaves de um dicionario com funções
for valores in dicionario.values():
    print(valores)

print(dicionario.values(), dicionario.keys())

print('' in dicionario)

# É possivel descobrir o tamanho do dicionário
print(len(dicionario))

# É possivel acessar os valores do dicionaio com a função items

for itens in dicionario.items():
    print(itens)
    # Já que é criado uma tupla dessa forma é possivel acessar chave e valor assim:
    print(itens[0], itens[1])

# Outra maneira de acessar chave e valor no dicionário
for chave, valor in dicionario.items():
    print(chave,valor)


clientes = {
    'cliente 1' : {
        'nome' : 'Ruanzin',
        'sobrenome' : 'Guedes'
    },
    'cliente 2' : {
        'nome' : 'Jonathas',
        'sobrenome' : 'Mandeta'
    }
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo: {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'{dados_k} = {dados_v}')

for clientes in clientes.items():
    print(f'\nExibindo: {clientes[0]}')
    for dados in clientes[1].items():
        print(f'{dados[0]} = {dados[1]}')

####################################################

# Alterando valores

dic = {'a' : 1,'b' : 2,'c' : 3,'d' : 4}

v = dic

# Em python, se você alterar po valor da variavel v que recebe o dicionario
# ambas mudarão de valor:

v['a'] ='Castanha'
print(dic,v)

# É possível fazer uma copia do dicionário:

dic2 = {'a' : 1,'b' : 2,'c' : 3,'d' : 4}
v2 = dic2.copy()

v2['a'] = 'One piece' 
print(dic2,v2)

# ALterando mesmo em uma copia

dic3 = {'a' : 1,'b' : 2,'c' : 3,'d' : 4, 'd' : ['Monge', 'Zenitsu']}
v3 = dic3.copy()

v3['b'] = 'Ruan'
v3['d'][0] = 'Evelin'

print(dic3,v3)

# Para criar uma copia de real é preciso importar o copy

v4 = copy.deepcopy(dic3)


# É possível transformar uma lista em um dicionário se ela possuir chave e valor:

lista = [
    ['l1','v1'],
    ['l2','v2'],
    ['l3','v3']
]
lista = dict(lista)
print(lista)

# removendo elemento do dicionário e juntando dicionários:
d1 = {
    1 : 2,
    3 : 4,
    5 : 6
}

d1.pop(5) # É preciso passar a chave
print(d1)
d1.popitem() # remove o ultimo elemento
print(d1)

d2 = {
    'a' : 'b',
    'c' : 'd',
    'e' : 'f',
    'g' : 'h'
}

d1.update(d2) # Desa forma você consgue concatenar dicionários
print(d1)
