from itertools import groupby
import itertools

notas_alunos = [
    {'nome' : 'Ruan', 'nota' : 'A'},
    {'nome' : 'Mael', 'nota' : 'B'},
    {'nome' : 'Minato', 'nota' : 'A'},
    {'nome' : 'Joni', 'nota' : 'C'},
    {'nome' : 'Samira', 'nota' : 'A'},
    {'nome' : 'Camila', 'nota' : 'D'},
    {'nome' : 'Dryelli', 'nota' : 'D'},
    {'nome' : 'Marcela', 'nota' : 'C'},
    {'nome' : 'Milena', 'nota' : 'A'},
    {'nome' : 'Fernando', 'nota' : 'B'},
    {'nome' : 'Penelop', 'nota' : 'A'}
]

ordena = lambda item: item['nota']
notas_alunos.sort(key=ordena)
# A função groupby vai criar várias listas com elemento de valores iguai, como no exemplo das notas

agrupados = groupby(notas_alunos, ordena)

for agrupamento, valores_agrupados in agrupados:
    print(f'Agrupamento: {agrupamento}')
    for aluno in valores_agrupados:
        print(aluno)
    print("")

for agrupamento, valores_agrupados in agrupados:
    print(f'Agrupamento: {agrupamento}')
    quantidade = len(list(valores_agrupados))