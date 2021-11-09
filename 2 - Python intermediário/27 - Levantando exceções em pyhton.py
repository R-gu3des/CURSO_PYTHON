# def divisao(n1, n2):
#     try:
#         return n1 / n2
#     except ZeroDivisionError as error:
#         print("Erro:", error)


#  Esse try except de fora da função vai relançar a exceção, pois foi usado função raise

# try:
#     print(divisao(5,0))
# except ZeroDivisionError as error:
#     print('Erro:', error)

def divisao(val1, val2):
    if val2 == 0:
        raise ValueError("Valor 2 não pode ser zero")
    return val1 / val2

try:
    print(divisao(5,0))
except ValueError as erro:
    print(erro)


