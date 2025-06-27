# CPF: 746.824.890-70

cpf = '74682489070'
nove_digitos = cpf[:9]
print(nove_digitos)

contador_regressivo_1 = 10
digitos_somados = 0
for digito in nove_digitos:
    digitos_somados += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

primeiro_digito = (digitos_somados * 10) % 11

primeiro_digito = primeiro_digito if primeiro_digito <= 9 else primeiro_digito = 0
