"""
Java Script Object Notation - JSON

JSON - É um formato de troca de dados entre sistemas
e programas muito leve e de fácil utilização. Muito utilizados por APIs
"""

from Dados_json import *
import json

lista = [1, 2, 3, 4, 5]

lista_pJson = json.dumps(lista)
print(lista_pJson)



with open('clientes.json', "w") as arquivo:
    json.dump(dicionario_clientes, arquivo, indent=4) # O indent serve para dizer qual o modo que vai saira estrutura do dicionario
    print

# Serve para trazer do json para o python
with open('clientes.json', "r") as arquivo:
    dados = json.load(arquivo) # O indent serve para dizer qual o modo que vai saira estrutura do dicionario
    print(dados)