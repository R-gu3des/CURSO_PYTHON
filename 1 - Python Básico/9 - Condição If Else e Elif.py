"""
Condição If ELSE e ELIF

"""
idade = 20


# If(significva - se). Essa expressão sempre tem que ser a primeira a ser passada para avaliar um condição
if idade == 20:
    print('Um jovem adulto!') 
elif idade == 10: # O elif(senão se...) funciona como um segmento de verificação do ultimo if
    print("Muito novo")
else: # o else(senão ...) é a continuação do ultimo elif ou if / Ele faz uma determinada ação se as anteriores não tiverem sido validadas
    print("Alguma coisa!")
