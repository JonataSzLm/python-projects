import re
import threading

import requests
from bs4 import BeautifulSoup

DOMINIO = 'https://django-anuncios.solyd.com.br'
URL_AUTOMOVEIS = 'https://django-anuncios.solyd.com.br/automoveis/'
LINKS = []
TELEFONES = []

def requisicao(url):
    try:
        reposta = requests.get(url)
        if reposta.status_code == 200:
            return reposta.text
        else:
            print('Erro ao fazer requisição')
    except Exception as e:
        print('Erro ao fazer requisição')
        print(e)

def parsing(resposta_html):
    try:
        soup = BeautifulSoup(resposta_html, 'html.parser')
        return soup
    except Exception as e:
        print('Erro ao fazer o parsing')
        print(e)

def encontrar_links(soup):
    try:
        cards_pai = soup.find('div', class_='ui three doubling link cards')
        cards = cards_pai.find_all('a', class_='card')
    except:
        print('Erro ao encontrar links')
        return None
    links = []
    for card in cards:
        link = card['href']
        links.append(link)

    return links

def encontrar_telefone(soup):
    try:
        descricao = soup.find_all('div', class_='sixteen wide column')[2].p.get_text().strip()

        regex = re.findall(r"\(?0?([1-9]{2})[ \-\.\)]{0,2}(9)[ \-\.]?(\d{4})[ \-\.]?(\d{4})", descricao)
        if regex:
            return regex

    except Exception as e:
        print('Erro ao encontrar descrição')
        return None


def descobrir_telefones():
    while True:
        try:
            link_anuncio = LINKS.pop(0)
        except:
            return None

        resposta_anuncio = requisicao(DOMINIO + link_anuncio)

        if resposta_anuncio:
            soup_anuncio = parsing(resposta_anuncio)
            if soup_anuncio:
                telefones = encontrar_telefone(soup_anuncio)
                if telefones:
                    for telefone in telefones:
                        print('Telefone encontrado: ', telefone)
                        TELEFONES.append(telefone)
                        salvar_telefone(telefone)

def salvar_telefone(telefone):
    telefone_str = '{}{}{}{}\n'.format(telefone[0], telefone[1], telefone[2], telefone[3])
    try:
        with open('telefones.csv', 'a') as arquivo:
            arquivo.write(telefone_str)
    except Exception as e:
        print('Erro ao salvar arquivo!')
        print(e)


if __name__ == '__main__':
    resposta_busca = requisicao(URL_AUTOMOVEIS)
    if resposta_busca:
        soup_busca = parsing(resposta_busca)
        if soup_busca:
            LINKS = encontrar_links(soup_busca)

            THREADS = []
            for i in range(10): # Criando 10 threads
                t = threading.Thread(target=descobrir_telefones)
                THREADS.append(t)

            for t in THREADS: # iniciando as threads
                t.start()

            # for t in THREADS: # esperando as threads
            #     t.join()
            #
            # print(TELEFONES)