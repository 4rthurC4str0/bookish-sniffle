import os

lista_de_compras = []

while True:
    lista_de_compras_enumerada = list(enumerate(lista_de_compras))
    print('Selecione uma opção')
    opção_selecionada = input('[i]nserir [a]pagar [l]istar: ')

    if opção_selecionada == 'i':
        os.system('clear')
        novo_item = input('Valor: ')
        lista_de_compras.append(novo_item)

    elif opção_selecionada == 'a':
        try:
            indice_str = input('Escolha o indice para apagar: ')
            indice_int = int(indice_str)
            del lista_de_compras[indice_int]
        except ValueError:
            os.system('clear')
            print('Digite um valor válido')
        except IndexError:
            os.system('clear')
            print('Digite um valor que existe')


    elif opção_selecionada == 'l':
        os.system('clear')
        if len(lista_de_compras) == 0:
            print('Nada para listar')

        for indice, valor in lista_de_compras_enumerada:
            print(indice, valor)
    
    else:
        print('Digite uma opção válida')