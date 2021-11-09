"""
and    | Significa 'e' / Analisa se duas  ou mais condições são verdadeiras
or     | Significa 'ou' / Analisa se pelo menos uma condição é verdadeiras
not    | Significa 'não' / Ele inverte a condição
in     | Significa 'dentro ou em' / Analisa se dterminado elemento está em ...
not in | Significa 'não esta em'

"""

a = 2
b = 3

# Caso sem o not. Irá analsisar se 3 é maior que 2
if b > a:
    print("3 é maior do que 2")
else:
    print("2 é maior do que 3")

# Caso com o not. Nesse caso analisa se b não é maior do que a
if not b > a:
    print("2 é maior do que 3")
else:
    print("3 é maior do que 2")


nome = 'Ruan'

if 'u' in nome: # Se 'u' estiver na variável nome...
    print('Existe a letra "u" no seu nome')


if 's' not in nome: # Se 's' nâo estiver no seu nome...
    print("Não existe a letra 's' no seu nome")