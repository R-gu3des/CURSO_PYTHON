"""
Entrada de Dados
"""

# from ast import copy_location

# nome = input("Digite o seu nome: ") # Por padrão a entrada de um input é uma string

# print(f'O usuário digitou {nome}.\nO tipo da variável é: {type(nome)}')


# # Podemos mudar o tipo de dado primitivo de uma variavel no input:

# idade = int(input("Digite a sua idade: "))
# Condicao_v_f = bool(input("Digite se a condição é True ou False: "))
# altura = float(input("Digite a sua altura: "))

# print(f'Tipo de idade: {type(idade)}\nTipo da condicao: {type(Condicao_v_f)}\nTipo de altura: {type(altura)}')

lista_inicial = [10, 5, -7, 6, -42, 63, -8, -5, 13]

lista_final = []

for item in lista_inicial:
    if item % 2 == 0:
        if item < 0:
            lista_final.append('A')
        else:
            lista_final.append('B')
    else:
        if item < 0:
            lista_final.append('C')
        else:
            lista_final.append('D')

print(lista_final)