"""
While / Else
contadores 
Acumuladores
"""

# Um contador serve como forma de iniciar e terminar um laço while.
# Um acumulador serve para acumular  os resultados do contador.

# Usando while om else:

contador = 0

while contador <= 10:
    print(contador)
    if contador == 5:
        break
    contador += 1
else:
    print("Estamos no else")

# Caso haja um break, o laço não vai executar o else

print("O laço acabou")
