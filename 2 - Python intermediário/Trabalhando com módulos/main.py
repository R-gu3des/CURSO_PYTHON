import vendas.calculospreco
vendas.calculospreco.aumento()

# Outra maneira de se exportar também:

from vendas import calculospreco

calculospreco.aumento()

from vendas.calculospreco import aumento, desconto, reducao

aumento()
desconto()
reducao()



# Para acessar uma funcao de um pacote que está dentro de outro
# é necessario percorrer pelo caminho de todos os pacotes Ex:
from vendas.formata.preco import real


print(real(55.00))

# É possivel nomear uma módulo como quiser após chama-lo em uma nova pasta Ex:

import vendas.formata.preco as prec

print(prec.real(55.00))