import requests
from bs4 import BeautifulSoup
import locale
from classes.modelos import FundoImobiliario, Scraper


locale.setlocale(category=locale.LC_ALL, locale='pt_BR.UTF-8')


def trata_porcentagem(porcentagem_str: str) -> float:
    parte_numerica = str(porcentagem_str.split("%")[0])
    return locale.atof(parte_numerica)

def trata_decimal(decimal_str: str) -> float:
    return locale.atof(decimal_str)


url_fundamentus = 'https://fundamentus.com.br/fii_resultado.php'
fundamentus = Scraper(url_fundamentus)
codigo_html = fundamentus.get_code_html()

linhas = codigo_html.find(id='tabelaResultado').find('tbody').find_all('tr')

for linha in linhas:
    dados_fundo = linha.find_all('td')

    codigo = dados_fundo[0].text
    segmento = dados_fundo[1].text
    cotacao = trata_decimal(dados_fundo[2].text)
    ffo_yield = trata_porcentagem(dados_fundo[3].text)
    dividend_yield = trata_porcentagem(dados_fundo[4].text)
    p_vp = trata_decimal(dados_fundo[5].text)
    valor_mercado = trata_decimal(dados_fundo[6].text)
    liquidez = trata_decimal(dados_fundo[7].text)
    qt_imoveis = trata_decimal(dados_fundo[8].text)
    preco_m2 = trata_decimal(dados_fundo[9].text)
    aluguel_m2 = trata_decimal(dados_fundo[10].text)
    cap_rate = trata_porcentagem(dados_fundo[11].text)
    vacancia = trata_porcentagem(dados_fundo[12].text)

    fundo_imobiliario = FundoImobiliario(codigo=codigo, segmento=segmento, cotacao=cotacao, ffo_yield=ffo_yield, dividend_yield=dividend_yield,
                                         p_vp=p_vp, valor_mercado=valor_mercado, liquidez=liquidez, qtd_imoveis=qt_imoveis,
                                         preco_m2=preco_m2, aluguel_m2=aluguel_m2, cap_rate=cap_rate, vacancia_media=vacancia
                                         )
