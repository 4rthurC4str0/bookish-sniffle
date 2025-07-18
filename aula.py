def parametros_decorador(nome):
    def decorador(func):
        print('Decorador:', nome)

        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return sua_nova_funcao
    return decorador

#cada decorador retorna uma nova função "embrulhada", que ao ser chamada retorna a função original adiconando algo novo

# é como se eu passase para o decorador_5, o decorador_4 e assim..
#Ao chamar soma(10, 5), você aciona a primeira camada (nome='5'), 
# que chama a segunda (nome='4'), que chama a terceira (nome='3'),  
# e assim por diante... até chegar na original soma(x, y).
@parametros_decorador(nome='5')
@parametros_decorador(nome='4')
@parametros_decorador(nome='3')
@parametros_decorador(nome='2')
@parametros_decorador(nome='1')
def soma(x, y):
    return x + y
#Cada chamada de "@parametros_decorador" você vai ter uma chamada de "sua_nova_funcao"
# Você tem 5 chamadas de funções "sua_nova_funcao" diferentes, uma dentro da outra - e cada uma lembra
#do seu próprio 'nome'


# quando eu chamo a função decorada soma(10, 5), na verdade eu estou chamando a função retornada
# pelo decorator, que envolve a original
dez_mais_cinco = soma(10, 5)
# quando isso é executado eu vejo o efeito de cada camada de decorator, mas eles não estão sendo 
#"executados de novo", só as funções "sua_nova_função", que eles retornaram
#pois cada decorator "@decorator" executa uma vez quando é definido e depois quando a função decorada
#é executada eu vejo o efeito de cada camada

print(dez_mais_cinco)
