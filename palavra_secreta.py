import os

palavra_secreta = 'floresta'
letras_acertadas = ''
numero_tentativas = 0

while True: 
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1
    
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formatada = ''
    for i in palavra_secreta:
        if i in letras_acertadas:
            palavra_formatada += i
        else:
            palavra_formatada += '*'
        
    print('Palavra formada: ', palavra_formatada)

    if palavra_formatada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOUUU!! PARABÉNS')
        print('A palavra era:', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0