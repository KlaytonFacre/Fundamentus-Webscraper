import requests
from bs4 import BeautifulSoup
from datetime import datetime
from tabulate import tabulate
import locale


locale.setlocale(category=locale.LC_ALL, locale='pt_BR.UTF-8')


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

    def __repr__(self):
        return f'[{self.codigo}] : {self.cotacao}'


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


class Estrategia:
    def __init__(self, segmento="", cotacao_min=0, ffo_yield_min=0, dividend_yield_min=0, p_vp_min=0,
                 valor_mercado_min=0, liquidez_min=0,
                 qtd_imoveis_min=0, preco_m2_min=0, aluguel_m2_min=0, cap_rate_min=0, vacancia_media_max=0):

        # Variáveis de instância da classe Estratégia que definirão o mínimo aceitável de cada valor do FII
        self.segmento = segmento
        self.cotacao_minimo = cotacao_min
        self.ffo_yield_minimo = ffo_yield_min
        self.dividend_yield_minimo = dividend_yield_min
        self.p_vp_minimo = p_vp_min
        self.valor_mercado_minimo = valor_mercado_min
        self.liquidez_minimo = liquidez_min
        self.qtd_imoveis_minimo = qtd_imoveis_min
        self.preco_m2_minimo = preco_m2_min
        self.aluguel_m2_minimo = aluguel_m2_min
        self.cap_rate_minimo = cap_rate_min
        self.vacancia_media_maxima = vacancia_media_max

    def aplica_estrategia(self, fundo: FundoImobiliario):
        if self.segmento != '':
            if fundo.segmento != self.segmento:
                return False

        if fundo.cotacao < self.cotacao_minimo\
                or fundo.ffo_yield < self.ffo_yield_minimo\
                or fundo.dividend_yield < self.dividend_yield_minimo\
                or fundo.p_vp < self.p_vp_minimo\
                or fundo.valor_mercado < self.valor_mercado_minimo\
                or fundo.liquidez < self.liquidez_minimo\
                or fundo.qtd_imoveis < self.qtd_imoveis_minimo\
                or fundo.preco_m2 < self.preco_m2_minimo\
                or fundo.aluguel_m2 < self.aluguel_m2_minimo\
                or fundo.cap_rate < self.cap_rate_minimo\
                or fundo.vacancia_media > self.vacancia_media_maxima:
            return False
        else:
            return True


class SalvaFundos:
    def __init__(self, fundos: list, caminho_arquivo: str):
        self.caminho_arquivo = caminho_arquivo
        self.fundos = fundos

    def salvar(self):
        with open(self.caminho_arquivo, 'a') as stream:
            tabela = []
            cabecalho = ['CODIGO', 'SEGMENTO', 'COTAÇÃO ATUAL', 'DIVIDEND YIELD']
            for fundo in self.fundos:
                tabela.append([
                    fundo.codigo,
                    fundo.segmento,
                    locale.currency(fundo.cotacao),
                    f'{locale.str(fundo.dividend_yield)} %'
                ])

            stream.write(f'FUNDOS APROVADOS EM {datetime.now()}\n')
            stream.write(tabulate(tabela, headers=cabecalho, tablefmt='fancy_grid', showindex='always'))
