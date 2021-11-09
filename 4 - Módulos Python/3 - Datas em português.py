from datetime import datetime
from locale import LC_ALL, setlocale, LC_ALL

setlocale(LC_ALL, "pt_BR.utf-8")

data = datetime.now()
formatado = data.strftime("%A, %d de %B de %Y")
print(formatado)
print(data)


# Pegar último dia do mês 

from calendar import mdays

data2 = datetime.now()
mes_atual = int(data2.strftime("%m"))

print((mdays[mes_atual]))
