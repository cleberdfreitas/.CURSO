import requests
import json
import os

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

# from modelos.restaurante import Restaurante
# from modelos.cardapio.bebida import Bebida
# from modelos.cardapio.prato import Prato

# restaurante_praca = Restaurante('praça', 'Gourmet')
# bebida_suco = Bebida('Suco de Melancia', 5.0,'grande')
# bebida_suco.aplicar_desconto()
# prato_paozinho = Prato('Paozinho',2.00,'O melhor pão da cidade')
# prato_paozinho.aplicar_desconto()
# restaurante_praca.adicionar_no_cardapio(bebida_suco)
# restaurante_praca.adicionar_no_cardapio(prato_paozinho)

def main():
    os.system('cls')
    # restaurante_praca.exibir_cardapio
    # print(response)

    if response.status_code == 200:
        dados_json = response.json()
        dados_restaurante = {}
        for item in dados_json:
            nome_do_restaurante = item['Company']
            if nome_do_restaurante not in dados_restaurante:
                dados_restaurante[nome_do_restaurante] = []

            dados_restaurante[nome_do_restaurante].append({
                "item": item['Item'],
                "price": item['price'],
                "description": item['description'],
            })
    else:
        print(f'o erro foi {response.status_code}')


    pasta_destino = "relatorios"

    # Verifica se a pasta já existe, se não, cria a pasta
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    for nome_do_restaurante, dados in dados_restaurante.items():
        nome_do_arquivo = f'{nome_do_restaurante}.json'
        caminho_completo = os.path.join(pasta_destino, nome_do_arquivo)
        with open(caminho_completo, 'w') as arquivo_restaurante:
            json.dump(dados, arquivo_restaurante, indent=4)

            

if __name__ == '__main__':
    main()