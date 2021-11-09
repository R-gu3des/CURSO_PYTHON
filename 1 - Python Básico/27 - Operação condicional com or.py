nome = input("Digite o seu nome: ")

print(nome or 'Você não digitou nada!') # Caso a primeira expressão seja falsa a segunda será exeutada

a = 0     #Expressão considerada !FALSA!
b = None  #Expressão considerada !FALSA!
c = False #Expressão considerada !FALSA!
d = []    #Expressão considerada !FALSA!  
e = {}    #Expressão considerada !FALSA!
f = 22
g = 'Luiz'

variavel = a or b or c or d or e or f or g
print(variavel)
