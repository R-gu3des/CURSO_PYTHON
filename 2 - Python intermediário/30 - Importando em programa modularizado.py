# Exemplo de modularização:

# Digamos que existem algumas partes do programa e pastas diferentes
# E a pasta 'main' onde será o programa inicial precisa ser executado
# se você precisar importar de uma pasta p1 para uma pasta p2 o caminho deve ser do ponto de vista do main
# Ex:
# 
# pasta1
#   funcaoes.py
#       somar()

# pasta2
#   funcaoes.py
#       listar

# main

# Para importar o somar para a pasta 2 precisa do caminho completo do ponto de vista do main
# from pasta1.funcoes import somar