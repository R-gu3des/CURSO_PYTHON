"""
Criando arquivos txt em python

Criando.
lendo,
escrevendo e
apagando
arquivos
"""


arquivo = open("arquivo_criado.txt","w+") 
# Essa é uma forma de criar um arquivo txt
# 1 - Primeiro passamos o nome do arqivo a ser criado
# 2 - Depois passamos o módulo a qual vai ser executado
# 3 - o "w+" permite que o arquivo possa ser escrito e lido  

# Escrevendo no arquivo txt criado

arquivo.write("Linha 1\n")
arquivo.write("Linha 2\n")
arquivo.write("Linha 3\n")
arquivo.write("Linha 4\n")

# Maneiras de ler o que está dentro do txt criado

# Isso acarreta em um erro. É não retorna nenhuma linha
# Necessitando passar a função .seek(0,0) o (0,0) indica a posição absoluta
# print("Lendo linhas: ")
# print(arquivo.read())

# Maneira de ler todas as linhas
arquivo.seek(0,0) # significa que o cursor vai para parte inicial
print(arquivo.read())

print("-=" * 15)

# Maneira de ler apenas uma linha:
arquivo.seek(0,0)
print(arquivo.readline(), end="")
print(arquivo.readline(), end="")
print(arquivo.readline(), end="")
print(arquivo.readline(), end="")
print("-=" * 15)


arquivo.seek(0,0)
arquivo.readlines # retorna um objeto iteravel

for linha in arquivo.readlines():
    print(linha, end="")

# No final ainda devemos fechar o aqquivo para não causar problemas ao código
arquivo.close()


# Muitos utilizam o bloco try para abrir um arquivo txt

# try:
#     new_Arquivo = open("abcd.txt", "w+")
#     new_Arquivo.write("ABCD")
#     new_Arquivo.seek(0,0)
#     print(new_Arquivo.read)
# finally:
#     new_Arquivo.close()


# Para abrir o arquivo já existente:
# Usando o with não é necessário fechar o arquivo no final
with open("abcd.txt","w+") as arq:
    arq.write("Morango\n")
    arq.write("Melância\n")
    arq.write("Banana\n")
    arq.write("Maçã\n")
    arq.seek(0)

    print(arq.read())

with open("abcd.txt", "r") as ar:
        ar.seek(0,0)
        print(ar.readline())

with open("abcd.txt", "a+", newline="") as arqui: # 'a' de append e continua adicionando varios elementos a lista
    arqui.write("Nova linha\n")
    arqui.write("Nova linha 2")

with open("abcd.txt","r") as lin:
    lin.seek(0,0)
    
    for c in lin.readlines():
        print(c, end="")



# Criando um arquivo de testo com json

import json

dicionario = {
    'Pessoa 1' : {
        'nome':'Amanda',
        'idade' : 21
    },
        'Pessoa 2' : {
        'nome':'Jonas',
        'idade' : 17
    }
}

dic_json = json.dumps(dicionario) # Transforma o dicionario em uma anotação do tipo json
print(dic_json)

with open('efg.json', 'w+') as js:
    js.write(dic_json)

with open('efg.json',"r") as efg:
    dic_json = efg.read()
    dic_json = json.loads(dic_json) # retransforma a anotação json em um objeto do tipo dicionário
    print(dic_json)


for c, v in dic_json.items():
    print(c)
    for ch, va in v.items():
        print(ch,va)