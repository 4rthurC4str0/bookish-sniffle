import os

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

questoes_acertadas = 0
for pergunta in perguntas:
    print(pergunta['Pergunta'])
    print(' ')
    print('Opções:')

    for indice, opc in enumerate(pergunta['Opções']):
        print(f'{chr(97 + indice)}) {opc}')

    for indice, opc in enumerate(pergunta['Opções']):
        letra_da_opc = chr(97 + indice)
        if pergunta['Resposta'] == opc:
            letra_da_resposta = letra_da_opc

    resposta = input('Escolha uma opção: ').lower()

    if resposta == letra_da_resposta:
        os.system('clear')
        print('Acertou')
        questoes_acertadas += 1
    else:
        os.system('clear')
        print('ERROU')



    # verifica se é a ultima pergunta para acabar o programa ou continuar respondendo
    if pergunta == perguntas[-1]:
        print(f'Você acertou: {questoes_acertadas} questões')
        print('acabou...')
        break
    else:
        resposta_continuar = input('Quer ir para a próxima pergunta? [s] [n]: ').lower().startswith('s')

        if resposta_continuar is True:
            continue
        else:
            print(f'Você acertou: {questoes_acertadas} questões')
            print('Você saiu...')
            break
