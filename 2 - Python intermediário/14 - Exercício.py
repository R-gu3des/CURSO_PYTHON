"""
Exercício - Manipulando strings
"""
string = '012345678901234567890123456789012345678901234567890123456789'
resultado = [string[i:i + 10] for i in range(0 ,len(string), 10)]
print(resultado)
final = '.'.join(resultado)
print(final)

# Outros métodos para utilizar o dictionary comprehension

dicionario_2 = {f'chave{x}': x ** 2 for x in range(10)}
print(dicionario_2)