Estados_e_Capitais = {
    "Acre": "Rio Branco",
    "Alagoas": "Maceió",
    "Amapá": "Macapá",
    "Amazonas": "Manaus",
    "Bahia": "Salvador",
    "Ceará": "Fortaleza",
    "Distrito Federal": "Brasília",
    "Espírito Santo": "Vitória",
    "Goiás": "Goiânia",
    "Maranhão": "São Luís",
    "Mato Grosso": "Cuiabá",
    "Mato Grosso do Sul": "Campo Grande",
    "Minas Gerais": "Belo Horizonte",
    "Pará": "Belém",
    "Paraíba": "João Pessoa",
    "Paraná": "Curitiba",
    "Pernambuco": "Recife",
    "Piauí": "Teresina",
    "Rio de Janeiro": "Rio de Janeiro",
    "Rio Grande do Norte": "Natal",
    "Rio Grande do Sul": "Porto Alegre",
    "Rondônia": "Porto Velho",
    "Roraima": "Boa Vista",
    "Santa Catarina": "Florianópolis",
    "São Paulo": "São Paulo",
    "Sergipe": "Aracaju",
    "Tocantins": "Palmas"
}

quer_continuar = True
rodadas = 0
acertos = 0

for estado, capital in Estados_e_Capitais.items():
        if not quer_continuar:
            break

        rodadas += 1
        print(f'\n -> Qual a Capital do Estado {estado}?')

        resposta = input ('Sua Resposta: ')
        if resposta.lower() == capital.lower():
            print('Resposta Correta!')
            acertos += 1
        else:
            print(f'Resposta Errada! O Correto seria {capital}')

        while True:
            opcao = input('Deseja continuar? (s/n)').lower()
            if opcao not in ['s', 'n']:
                print('Responda apenas com "s" para sim ou "n" para não.')
                continue
            elif opcao == 'n':
                quer_continuar = False
            break

if rodadas > 0:  # Evitar divisão por zero
    porc = acertos / rodadas * 100
else:
    porc = 0

print(f'Você acertou {acertos} de {rodadas}')
print(f'Porcentagem de acertos: {porc:.2f}%')
