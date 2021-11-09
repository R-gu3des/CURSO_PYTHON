"""
Funções - parte 3

Parametros -> *args e **kwargs

"""

def func(a1,a2,a3,a4,a5, nome = None, a6 = None):
    print(a1,a2,a3,a4,a5, nome, a6)
    return nome, a6 # É posível passar mais de um parâmetro no return

func(1,2,3,4,5, nome="Ruan",a6= 'Robô')    

# Quando não se sabe quantos argumentos serão passados em uma função
def funcTeste(*args):
    print(args)
    print(args[0])
    print(args[-1]) # Para acessar os argumentos é necessário passar a posição
    print(len(args)) # É possível passar a quantidade de elementos que tem em args
    # Não é possível alterar o valor de args, pois é uma tuplas, mas é posível transformar o valor em uma lista e altera-lo  

funcTeste('Ruan',22 , 30, 'roger', 10.5)

lista = [1, 2, 3, 4, 5, 6, 7]

print(*lista, sep='-') # Print com asteristco antes, remove todas as marcas, sep é oque será usado para separar os argumentos

def funcTeste2(*args, **kwargs):
    # O kwargs serve para passar chaves e valores, esses nomes não são oficiais apenas precisa dos asteristicos para diferenciar
    print(args)
    print(kwargs)
    print(kwargs['nome'], kwargs['idade'])
    # Se tiver o atrubuto idade por exemplo é possível pegar assim:
    # para não aparecer erro:
    nome = kwargs.get('nome')

    if nome is not None:
        print(nome)
    else:
        print('Nome não existe')

funcTeste2(1, 2, 3, 4, 5, 6, nome = 'Ruan', idade = 26)
