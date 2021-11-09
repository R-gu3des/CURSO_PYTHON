# Não se deve usar parâmetros mutaveis em uma função. Pode dar erro
# Ex:

# Atributos mutáveis: listas, dicionários...
# Atributos imutáveis: tuplas, None, strings, numeros, booleanos


def listaDeFuncoes(clientes_iteraveis, lista = []):
    lista.extend(clientes_iteraveis)
    return lista


cliente_1 = listaDeFuncoes(['Jonas',"Marcos",'Hernandes'])
cliente_2 = listaDeFuncoes(['Janaina','Cláudia','Maria'])

print(cliente_1)
print(cliente_2)

# Dessa maneira ambas as listas se juntaram


# Para resolver isso basta fazer umas mudanças:

def listaDeFuncoes(clientes_iteraveis, lista = None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteraveis)
    return lista


cliente_1 = listaDeFuncoes(['Jonas',"Marcos",'Hernandes'])
cliente_2 = listaDeFuncoes(['Janaina','Cláudia','Maria'])

print(cliente_1)
print(cliente_2)

