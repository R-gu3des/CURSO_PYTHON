"""
Tipos de dados:

str   | String   - Palavras
int   | Inteiro  - Número sem casas decimais
float | Float    - real/ponto flutuante
bool  | booleano - Operador Lógico (True ou False)

"""

print(type('Maria'))
print(type(10))
print(type(11.0))
print(type(True))

print(10 == '10') # A condição == não é uma atribuição e sim uma pergunta, nesse caso retorna um booleano


#  Conversão do tipo da variavel (type casting)
numero = '10'
numero2 = int(numero)

print(type(numero2))
print()