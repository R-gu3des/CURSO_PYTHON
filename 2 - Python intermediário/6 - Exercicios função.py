def funcao1(func, *args,**kwargs):
    return func(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome,saudacao):
    return f'{saudacao}, {nome}'

print(funcao1(fala_oi,'Luiz')) # Aqui esta sendo passado uma funcao como parametro, e um parametro que será passad para a proxima função
print(funcao1(saudacao,'Mario', 'Oi amigo!'))