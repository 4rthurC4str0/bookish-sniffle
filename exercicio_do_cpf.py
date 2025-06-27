# CPF: 746.824.890-70

cpf = '74682489070'
digitos = []

for digito in cpf:
    digitos.append(int(digito))
    for i, digit in enumerate(digitos):
        if i == 9 or i == 10:
            del digitos[i]

print(digitos)

digitos_multiplicados = []
contador = 10
for i, digito in enumerate(digitos):
    novo_digito = digito * contador
    digitos_multiplicados.insert(i, novo_digito)
    contador -= 1

print(digitos_multiplicados)

soma_digitos = 0
for digito in digitos_multiplicados:
    soma_digitos += digito
print(soma_digitos)

multiplacacao_da_soma = soma_digitos * 10
print(multiplacacao_da_soma)

resto_divisao_onze = multiplacacao_da_soma % 11
print(resto_divisao_onze)

if resto_divisao_onze > 9:
    digitos.append(0)
else:
    digitos.append(resto_divisao_onze)

print(digitos)

novo_cpf = ''
for digito in digitos:
    novo_cpf += str(digito)

print(novo_cpf)