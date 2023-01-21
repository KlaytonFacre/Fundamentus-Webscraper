import requests
from bs4 import BeautifulSoup


url = 'https://fundamentus.com.br/fii_resultado.php'
headers = {
    'User-Agent': "Mozilla/5.0"
}

resposta = requests.get(url=url, headers=headers)

soup = BeautifulSoup(resposta.text, 'html.parser')

linhas = soup.find(id='tabelaResultado').find('tbody').find_all('tr')

for linha in linhas:
    row_fundo = linha.find_all('td')
    print(
        f'[{row_fundo[0].text}]:\n',
        f'\tSegmento: {row_fundo[1].text}\n',
        f'\tCotação: R$ {row_fundo[2].text}\n',
        f'\tDY %: {row_fundo[4].text}\n',
        f'\tP/VP: {row_fundo[5].text}\n',
        f'\tValor de Mercado: R$ {row_fundo[6].text}\n',

    )
