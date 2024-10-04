import os
import json
import requests

from fastapi import FastAPI, Query

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    endpont, msg
    '''
    return{'Hello':'World'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    endpont, para ver os cardapios
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        dados_json = response.json()
        
        if restaurante is None:
            return{'Dados':dados_json}

        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
        return {'Restaurante':restaurante,'Cardapio':dados_restaurante}
    else: 
        return {'Erro':f'{response.status_code} - {response.text}'}