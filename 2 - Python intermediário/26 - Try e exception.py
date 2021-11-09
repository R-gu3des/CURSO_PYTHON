"""
Utilizando Try

Try - Siginifica tentar em inglês -> O Try tenta executar uma ação e caso dê errado ele vai para a exceção
except - Significa exceção --> Quando ocorre um erro você pode executar uma ação(passar - pass, printar erro etc...)

"""

#Usando o try except

try:
    print(a) # nesse caso acontece um erro, pois a variavel 'a' não existe
except:
    print("Elemento não encontrado")


try:
    print(a) # nesse caso acontece um erro, pois a variavel 'a' não existe
except NameError as erro:
    print("Erro:",erro)

print("Código continuando")

# Pode se utilizar mais de um except

b  = {}
try:
    print(b[1])
except NameError as err:
    print("Erro:",err)
except (IndexError, KeyError): # É possivel passar mais de um erro em um except 
    print("Erro de índice ou chave")
except:
    pass
else:
    print("Seu código foi executado com sucesso") # Caso não exista nem uma excessão a ser tratada, o else será executado
finally:
    print("Finalmente") # O finally sempre será executado independente do que occorrer nesta parte do código

# se houver um try e except dentro de outro try ou except e ocorrer um erro o código dserá parado

