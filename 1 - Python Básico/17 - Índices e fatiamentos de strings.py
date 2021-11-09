"""
Manipulando strings

* String indices - Um índice é a quantidade de elementos que uma string/lista/dicionario possuem.
* O índice começa em 0 e não em 1 - Indice = quantidade de elementos - 1.
* Fatiamento de Strings - [Inicio:fim:passo] : Essa é a maneira de acessar uma posição em um elemento "[]"

"""

#  Ex:
string = 'A vida é um caos aleatório, ordenada pelo tempo'

# Quero pegar só a parte "aleatório"
print(string[17:26]) # Temos que colocar um espaço a mais se não não pegará o ultimo elemento


# Podemos mostrar o elemento ao contrario:
print(string[::-1]) # Podemos percorrer o elemento ao contrario. 
# Se não pasarmos o valor antes e depois dos dois pontos o padrão para inicio = 0 e fim = maximo de cacracteres

# Pegando ultimo caractere
print(string[-1])

# Podemos escolher de quanto em quantos caracteres serão escolhidos, passando o valor na ultima posição

print(string[::2]) # Vai pular de 2 em 2