"""
Utilizando a função map
"""

from Dados import pessoas, produtos, lista

nova_lista = map(lambda x: x * 2, lista) # É preciso passar a lista como argumento

# Nesse caso ao map não retorna uma lista e sim um objeto:

print(lista)
print(list(nova_lista)) # Transformando o objeto em lista



"""Usando dicionário"""

precos = map(lambda x: round(x['preco'] * 1.05), produtos) # com um lambda não é possivel alterar o preço dos produtos
for p in precos:
    print(p)

def aumenta_prec(prod):
    prod['preco'] = round(prod['preco'] * 1.05, 2) # A função round faz um arredonadamento de um float -> O "2" indica o número de casas decimais
    return prod

novos_produtos = map(aumenta_prec, produtos)

for c in novos_produtos:
    print(c)



"""Criando uma lista só com os nomes em pessoas """

lista_nomes =list(map(lambda x: x['nome'], pessoas))
print(pessoas)