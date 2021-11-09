"""
Escopo em uma função python
"""
variavel = 'valor 1'

# Nesse casoa a função consegue acessar "variavel", por se tratar de uma variavel global
def funcao1():
    print(variavel)

# Nesse caso a função vai pegar o valor mais próximo
def funcao2():
    variavel = 'outro valor'
    print(variavel)

funcao1()
funcao2()

################################################

variavel2 = 'var 2'

def func():
    print(variavel2)
    variavel2 = 'New value'
    print(variavel2)
    # Nesse caso você pode pensar que a variavel global será executada.
    # Porém ocorrerá um erro(Dizendo que a variavel foi acessada antes de ser criada)

# Uma variavel definidda em uma função não pode ser acessada por outra função, pois não está disponívvel no escopo global