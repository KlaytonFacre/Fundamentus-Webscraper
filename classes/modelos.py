import requests
from bs4 import BeautifulSoup


class FundoImobiliario:
    def __init__(self, codigo, segmento, cotacao, ffo_yield, dividend_yield, p_vp, valor_mercado, liquidez,
                 qtd_imoveis, preco_m2, aluguel_m2, cap_rate, vacancia_media):

        # Variáveis de instância da classe FundoImobiliário
        self.codigo = codigo
        self.segmento = segmento
        self.cotacao = cotacao
        self.ffo_yield = ffo_yield
        self.dividend_yield = dividend_yield
        self.p_vp = p_vp
        self.valor_mercado = valor_mercado
        self.liquidez = liquidez
        self.qtd_imoveis = qtd_imoveis
        self.preco_m2 = preco_m2
        self.aluguel_m2 = aluguel_m2
        self.cap_rate = cap_rate
        self.vacancia_media = vacancia_media


class Scraper:
    def __init__(self, url: str):

        self.url = url
        self.resposta = None
        self.header = {
            'User-Agent': "Mozilla/5.0"
        }

    def get_code_html(self):
        self.resposta = requests.get(url=self.url, headers=self.header)

        return BeautifulSoup(self.resposta.text, 'html.parser')
