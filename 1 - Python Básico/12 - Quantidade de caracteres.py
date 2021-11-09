"""
Quantidade de caracteres
"""
# O método len serve para retornar a quantidade de caracteres de uma string, array, lista e etc


nome = input("Digite o seu nome: ")
quantd_caracteres = len(nome)

print(f'O nome {nome} possui {quantd_caracteres} caracteres')
print(f'O tipo de primitivo retornado em len é {type(quantd_caracteres)}') 
#  Espaços vazios contam como caracteres
# O len retorna um inteiro

valor = 123456

print(len(valor)) #Len não consegue fazer a contagem de uma variavel que possui um número
# Booleano também não funciona