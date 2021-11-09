#        Índices
#        0123456789......................33

frase = 'O rato roeu a roupa do rei de roma'

contador = 0
novaString = ''

letra = input('Qual letra você deseja colocar em maiuscula: ')

while contador < len(frase):
    if frase[contador] == letra:
        novaString += letra.upper()
    else:
        novaString += frase[contador] # o operador += também serve para juntar strings
    contador+=1

print(novaString)