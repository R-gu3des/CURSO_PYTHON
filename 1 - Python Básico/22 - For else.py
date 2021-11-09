"""
For / Else em python
"""

lista = ["Mariana", 'Samaro', 'Jone depp']

for elem in lista:
    if elem.startswith('M'): # A função startswith checa se o elemento inicia com determinado caractere
        print(f'O nome {elem} inicia com a letra M')
    else:
        print("Não começa com M")

for elem in lista:
    if elem.lower().startswith('j'):
        print(f'O nome {elem} inicia com a letra j')
else:
    print("Não começa com j")

# Se todo o laço termnar e o laço não for quebrado, o else será executado