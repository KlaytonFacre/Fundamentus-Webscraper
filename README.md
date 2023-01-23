# Webscraping
 Webscraping de dados financeiros de FIIs do site fundamentus.com.br utilizando python.

O objetivo é extrair as informações sobre FII disponíveis [na página](https://fundamentus.com.br/fii_resultado.php) e armazenar em Objetos FundoImobiliário dentro do programa.

## Funcionamento

O programa:
1. Faz a requisição GET para a página do site
2. Recebe os dados e armazena
3. Busca o código HTML pelos dados dos FIIs
4. Armazena temporariamente em um Objeto FundoImobiliario
5. Verifica se os dados do FII atende ao mínimo definido na classe Estratégia
6. Se sim, armazena em uma lista
7. Se não, descarta o objeto

Ao final temos uma lista que é printada na tela do terminal com todos os fundos listados na página **que atendem à estratégia**. Adicionei a funcionalidade de também permitir que os dados sejam salvos em um arquivo .TXT

## Bibliotecas utilizadas
* Requests
* BeautifulSoup 4
* Tabulate
