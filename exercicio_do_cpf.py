# CPF: 746.824.890-70
import random

nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0, 9))

contador_regressivo_1 = 10
digitos_somados_1 = 0
for digito in nove_digitos:
    digitos_somados_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

primeiro_digito = (digitos_somados_1 * 10) % 11

primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0

dez_digitos = nove_digitos + str(primeiro_digito)

contador_regressivo_2 = 11
digitos_somados_2 = 0
for digito in dez_digitos:
    digitos_somados_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

segundo_digito = (digitos_somados_2 * 10) % 11

segundo_digito = segundo_digito if segundo_digito <= 9 else 0

cpf_gerado_calculo = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

print(cpf_gerado_calculo)
