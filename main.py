import requests
from bs4 import BeautifulSoup

def retorna_html(url):
    page = requests.get(url)
    if page.status_code == 200:
        print(f"Sucesso ao acessar a URL: {url}")
        return page.text
    else:
        print(f"Erro ao acessar a URL: {url}. Código de status: {page.status_code}")
        return None
    
def energia_solar():
    url = "https://canalsolar.com.br/noticias/"
    html = retorna_html(url)
    soup = BeautifulSoup(html, "html.parser")
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
            conteudo.append((titulo, data, link))

    return conteudo

if __name__ == "__main__":
    lista = energia_solar()
    print(lista)