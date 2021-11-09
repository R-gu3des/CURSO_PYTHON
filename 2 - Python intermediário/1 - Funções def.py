"""
Defininfo funções
"""

def saudacao(mensagem, nome):
    print(mensagem, nome)

saudacao("Parbéns! você conseguiu", 'Ana')

# Você pode passar valores padrões para casa não sejam passados os parâmetros da função
def somar(num1 = 1 , num2 = 1):
    return num1 + num2

print(somar(5,7))
print(somar())
 