"""Implementando conhecimentos com dicionário"""

print("Texto explicativo\n")
acertos = 0

perguntas = {
    'pergunta 1' : {
        'pergunta' : 'Quanto é 2 + 2',
        'resposta' : {'a' : 5,'b' : 4,'c' : 10,'d' : 8},
        'resposta certa' : 'b'
    },
    'pergunta 2' : {
        'pergunta' : 'Anime de pratas com mais de 900 episódios',
        'resposta' : {'a' : 'Jujustu kaisen','b' : 'Boku no hero','c' : 'Naruto shippuden','d' : 'One piece'},
        'resposta certa' : 'd'
    },
    'pergunta 3' : {
        'pergunta' : 'Maior plataforma de música',
        'resposta' : {'a' : 'Stremio','b' : 'utorrent','c' : 'Spotfy','d' : 'Netflix'},
        'resposta certa' : 'c'
    },
    'pergunta 4' : {
        'pergunta' : 'Que operação matematica é essa? 2 * 88',
        'resposta' : {'a' : 'multiplicação','b' : 'Subtração','c' : 'Soma','d' : 'Divisão'},
        'resposta certa' : 'a'
    },
    'pergunta 5' : {
        'pergunta' : 'Quem foi Michael Jackson',
        'resposta' : {'a' : 'Raper','b' : 'Dançarino','c' : 'Jogador de futebol','d' : 'Rei do pop'},
        'resposta certa' : 'd'
    }
}

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    print('Escolha as opções abaixo:\n')
    for rk, rv in pv["resposta"].items():
        print(f'{rk}) {rv}')
    sua_resposta = input('\nDigite a sua resposta: ')
    if sua_resposta == pv['resposta certa']:
        print(f'\nVocê acertou!!\nResposta correta: {pv["resposta certa"]}')
        acertos += 1
    else:
        print(f'\nVocê errou!!\nResposta correta: {pv["resposta certa"]}')
    print('')

quantidade_de_perguntas = len(perguntas)
porcentagem_acertos = acertos/quantidade_de_perguntas * (100)
print(f"A porcentagem total de acertos foi: {porcentagem_acertos}%.")