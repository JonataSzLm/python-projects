import json
import sys

import requests

URL_ALL = 'https://restcountries.com/v2/all'
URL_NAME = 'https://restcountries.com/v2/name'

def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
    except:
        print('Erro ao realizar requisição em:', url)

def parsing(texto_da_resposta):
    try:
        return json.loads(texto_da_resposta)
    except:
        print('Erro ao fazer parsing')

def contagem_de_paises():
    resposta = requisicao(URL_ALL)
    if resposta:
        lista_de_pais = parsing(resposta)
        if lista_de_pais:
            return len(lista_de_pais)
        else:
            print('0')

def listar_todos_paises(lista_de_paises):
    for pais in lista_de_paises:
        print(pais['name'])

def mostrar_populacao(nome_do_pais):
    resposta = requisicao('{}/{}'.format(URL_NAME, nome_do_pais))
    if resposta:
        lista_de_pais = parsing(resposta)
        if lista_de_pais:
            for pais in lista_de_pais:
                print('{}: {}'.format(pais['name'], pais['population']))
        else:
            print('País não encontrado')

def mostrar_moedas(nome_do_pais):
    resposta = requisicao('{}/{}'.format(URL_NAME, nome_do_pais))
    if resposta:
        lista_de_pais = parsing(resposta)
        if lista_de_pais:
            for pais in lista_de_pais:
                print('Moedas do {}: '.format(pais['name']))
                moedas = pais['currencies']
                for moeda in moedas:
                    print('{} - {}'.format(moeda['name'], moeda['code']))
        else:
            print('Moedas não encontrado')

def ler_nome_pais():
    try:
        nome_pais = sys.argv[2]
        return nome_pais
    except:
        print('É precisso passar o nome do país!')

if __name__ == "__main__":

    if len(sys.argv) == 1:
        print('### BEM VINDO AO SISTEMA DE PAISES ###')
        print("Uso: python paises.py <ação> <nome do pais>")
        print('Ações disponiveis:\n contagem, moeda, populacao')
    else:
        argumento1 = sys.argv[1]

        if argumento1 == 'contagem':
            numero_paises  = contagem_de_paises()
            print('Existem {} países no mundo todo!'.format(numero_paises))
        elif argumento1 == 'moeda':
            pais = ler_nome_pais()
            if pais:
                mostrar_moedas(pais)
        elif argumento1 == 'populacao':
            pais = ler_nome_pais()
            if pais:
                mostrar_populacao(pais)
        else:
            print('Argumento Inválido!')
