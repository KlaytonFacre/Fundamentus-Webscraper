import requests
from bs4 import BeautifulSoup


class Fii:
    def __init__(self, codigo=None, segmento=None, cotacao=None, dy=None, pvp=None, valor_mercado=None):
        self.codigo = codigo
        self.segmento = segmento
        self.cotacao = cotacao
        self.dy = dy
        self.pvp = pvp
        self.valor_mercado = valor_mercado

    def __repr__(self):
        return f'[{self.codigo}] : R$ {self.cotacao}'

    def print_data(self):
        print(
            f'[{self.codigo}]:\n',
            f'\tSegmento: {self.segmento}\n',
            f'\tCotação: R$ {self.cotacao}\n',
            f'\tDY %: {self.dy}\n',
            f'\tP/VP: {self.pvp}\n',
            f'\tValor de Mercado: R$ {self.valor_mercado}\n',
        )


class WebScraper:
    def __init__(self, url):
        self.headers = {
            'User-Agent': 'Mozilla/5.0'
        }
        self.url = url
        self.response = None
        self.soup = None

    def scrap_table(self):
        self.response = requests.get(self.url, headers=self.headers)
        self.soup = BeautifulSoup(self.response.text, "html.parser")
        table = self.soup.find("table", id="tabelaResultado")
        return table

    def print_table_data(self):
        table = self.scrap_table()
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            for cell in cells:
                print(cell.text)

    def fetch_list(self) -> list:
        resultado = []
        self.scrap_table()
        linhas = self.soup.find('tbody').find_all('tr')
        for linha in linhas:
            lista_temporaria = linha.find_all('td')
            fii_temporario = Fii(codigo=lista_temporaria[0].text, segmento=lista_temporaria[1].text,
                                 cotacao=lista_temporaria[2].text, dy=lista_temporaria[4].text,
                                 pvp=lista_temporaria[5].text, valor_mercado=lista_temporaria[6].text)
            resultado.append(fii_temporario)

        return resultado


site_alvo = 'https://fundamentus.com.br/fii_resultado.php'
scraper = WebScraper(site_alvo)
lista = scraper.fetch_list()
for fii in lista:
    fii.print_data()
