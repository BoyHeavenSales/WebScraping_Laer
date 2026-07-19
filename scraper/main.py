import requests
import csv
from bs4 import BeautifulSoup

def retorna_html(url):
    page = requests.get(url)
    if page.status_code == 200:
        print(f"Sucesso ao acessar a URL: {url}")
        return page.text
    else:
        print(f"Erro ao acessar a URL: {url}. Código de status: {page.status_code}")
        return None

def soup_url(url):
    html = retorna_html(url)
    if html:
        return BeautifulSoup(html, "html.parser")
    else:
        return None

def energia_solar():
    url = "https://canalsolar.com.br/noticias/"
    soup = soup_url(url)
    noticias = soup.find("div", "elementor-element elementor-element-653ee24 e-flex e-con-boxed e-con e-child").find_all("h2")
    # Links para as principais notícias
    links = [l.a['href'] for l in noticias]
    # Conteudo a ser retornado
    conteudo = []
    # Navegando pelos links das notícias e extraindo o conteúdo
    for link in links:
        html_noticia = retorna_html(link)
        if html_noticia:
            soup_noticia = BeautifulSoup(html_noticia, "html.parser")
            titulo = soup_noticia.find("h1", class_="elementor-heading-title elementor-size-default").text.strip()
            data = soup_noticia.find("span", class_="elementor-icon-list-text elementor-post-info__item elementor-post-info__item--type-date").text.strip()
            conteudo.append([titulo, data, link])

    return conteudo

def energia_eolica():
    url = "https://abeeolica.org.br/categoria/noticias/agencia-abeeolica/"
    soup = soup_url(url)
    noticias = soup.find_all("div", class_="col-12 col-md-6 col-lg-4")
    # Links para as principais notícias
    links = [l.a['href'] for l in noticias]
    # Conteudo a ser retornado
    conteudo = []
    # Navegando pelos links das notícias e extraindo o conteúdo
    for noticia in noticias:
        data_noticia = noticia.find("span", "date").text.strip()
        conteudo.append([noticia.find("h5").text.strip(), data_noticia, noticia.a["href"]])

    return conteudo

def gravar_resultado(lista, adress):
    # Guardando o conteúdo em um arquivo de texto
        with open(adress, "r", encoding="utf-8") as arq:
            lista_noticias_atuais = csv.reader(arq)
            lista_links_csv = [linha[3].strip() for linha in lista_noticias_atuais]
            lista_noticias_do_dia  = []
            for titulo, data, link in lista:
                if link not in lista_links_csv:
                    lista_noticias_do_dia .append([titulo,data,link])
        
        # print(lista_links_csv)

        with open(adress, "w", encoding="utf-8") as arq:
            for noticia in lista_noticias_do_dia:
                arq.write(f'{noticia[0]},{noticia[1]},{noticia[2]}\n')

if __name__ == "__main__":
    lista_solar = energia_solar()
    lista_eolica = energia_eolica()
    # gravar_resultado(lista_solar, "database/noticias_solar.csv")
    # print(lista_solar)
    # print(lista_eolica)
    gravar_resultado(lista_eolica, "database/noticias_eolica.csv")

    