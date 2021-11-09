"""
Mais informações em: https://docs.python.org/3.0/library/datetime.html
"""

from datetime import date, datetime, time, timedelta

# ENTRADA => ANO-MES-DIA HORA:MIN:SEGUNDO
data = datetime(2021,9,3,20,3,20)

print(data)
# SAÍDA => 2021-09-03 20:03:20

# Como o padrão de saída é o EUA precisamos de algum método para formatar para o PT-BR

dataBr = data.strftime('%d/%m/%Y %H:%M:%S') # O método strftime converte uma data para o formato que vc quiser

# O '%' é o indicador que precisa ser utilizado antes de escolher entre d(dia), m(mês), Y(ano), H(hora)
# M(minuto), S(segundo). Não necessariamente precisa ser barra para dividir ou os dois pontos.

print(dataBr)
print("+=" * 20,"\n")

# É possível passar uma data em forma de string e atribuir os valores para elas(dia, ano, mês)

novaData = datetime.strptime("03/09/2021", "%d/%m/%Y") # O método strptime converte de string para data
print(novaData)

# Também é possível converter a data para segundos, que no caso é contado desde 01-01-1970 até a data enviada

print(novaData.timestamp())

# Também é possível passar o contrário

data_3 = datetime.fromtimestamp(1630638000.0)
print(data_3)


"""
Brincando um pouco com as datas

"""
datax = datetime.strptime('22/05/2000 20:46:35', '%d/%m/%Y %H:%M:%S')

# Digamos que você queira adicionar mais alguns dias a esta data, ou alguns segundos...

data_mais_5_minutos = datax + timedelta(days=5, seconds=55) 
print('data 1 = ' , datax, 'data 2 =', data_mais_5_minutos)

# É possível calcularmos a diferença entre as datas

diferenca = datax - data_mais_5_minutos
print(diferenca) # Diferença de dias e horas
print(diferenca.days) # Só a diferença de dias

# Também podemos comparar se uma data é maior que a outra

print(data_mais_5_minutos > datax)
# SAÍDA => True