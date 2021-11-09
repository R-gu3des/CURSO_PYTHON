"""
Exércicio - 3
"""


cpf = input("Digite um cpf válido: ")

cpfIni = []
soma = 0
for c in range(11):
    if cpf[c].isnumeric():
        cpfIni.append(cpf[c])

for i, c in enumerate(cpfIni):
    valorInverso = 10 - i
    soma += (int(c) * valorInverso)

resultado = 11 - (soma % 11)
digit = 0
digit = 0 if resultado > 9 else resultado