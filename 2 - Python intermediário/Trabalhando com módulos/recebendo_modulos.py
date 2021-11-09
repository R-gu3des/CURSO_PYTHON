import Criando_modulos as mdl


# Ao executar o modulo exportado, tudo que está dentro dele também serrá executado
print(mdl.PI)
print(__name__)

lista = [ 2,4,6]

print(mdl.dobraLista(lista))

# Também podemos chamar desta forma

from Criando_modulos import multiplica_lista

print(multiplica_lista([2,4,6]))