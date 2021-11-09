carrinho = []
soma = 0
carrinho.append(('Camisa', 39.50))
carrinho.append(('Mochila', 110.25))
carrinho.append(('Vestido', 90))
carrinho.append(('Calça', 100))
carrinho.append(('Cueca', 45))
carrinho.append(('Casaco', 150))

resultado = sum([float(y) for x,y in carrinho ])

print(resultado)