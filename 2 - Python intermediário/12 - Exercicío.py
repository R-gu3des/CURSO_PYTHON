lista_inteiros = [
    [1,2,3,4,5,6,7,8,9,10],
    [9,1,0,9,9,7,2,1,6,8],
    [1,3,2,2,8,6,5,9,6,7],
    [3,8,2,8,6,5,9,6,7],
    [4,8,8,8,5,1,10,3,1,7],
    [1,3,7,2,2,1,5,1,9,9],
    [10,2,2,1,3,5,10,10,1]
]
analisador = []

for c in range(len(lista_inteiros)):
    resultado = -1
    for j in lista_inteiros[c]:
        if j in analisador:
            resultado = j
            print(f'{lista_inteiros[c]} --> {resultado}')
            analisador.clear()
            break
        else:
            analisador.append(j)
    if resultado == -1:
        print(f'{lista_inteiros[c]} --> {resultado}')
        analisador.clear()
