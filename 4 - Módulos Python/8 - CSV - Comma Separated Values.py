"""
Comma Separeted Values - CSV (Valores separados por vírgula)
É um formato de dados muito usado em tabelas (Excel, Google, Sheets), base de dados, clientes de e-mall, etc...
"""
import csv

lista = []
with open('Pasta1.csv', 'r') as arquivo:
    dados = csv.reader(arquivo) # O csv.reader cria um objeto que pode ser iterado
    
    for dado in dados:
        # métodos para adicionar listas dentro de outra lista
        lista += [dado] 
        print(dado)
        # lista.append(dado)
    print("lista: ",lista[1:])

print(lista)


# =======================================================================================================


lista = []
with open('Pasta2.csv', 'r') as arquivo:
    dados2 = csv.DictReader(arquivo) 

    for dado in dados2:
        print(f"Fruta: {dado['Frutas']} // Preço: {dado['preco']}")
        


# =========================================================================================================

with open('Pasta1.csv','r') as pasta:
    dados = [x for x in csv.DictReader(pasta)]

with open('Pasta3.csv', "w") as arq:
    escreve = csv.writer(
        arq,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
        
    )
    print(dados)
    chaves = dados[0].keys()
    chaves = list(chaves)
    
    for dado in dados:
        escreve.writerow(
            [
               dado[chaves[0]],
               dado[chaves[1]],
               dado[chaves[2]],
               dado[chaves[3]] 
            ],

        )