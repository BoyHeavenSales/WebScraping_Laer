import csv

def retornar_noticias(adress):
    with open(adress, 'r', encoding="utf-8") as arq:
        noticias = list(csv.reader(arq))
        mensagem = ""
        if len(noticias) >= 3:
            for i in range(3):
                mensagem += f'📰 {noticias[i][0]}\n📎: {noticias[i][-1]}\n\n'
        else:
            mensagem = "U+26A0 Sem noticias novas!"

        return mensagem
        

def criar_mensagem():
    # Vou focar em apenas as três primeiras noticias
    noticias_eolica = retornar_noticias("database/noticias_eolica.csv")
    if noticias_eolica:
        mensagem = "💨 *Últimas notícias sobre energia eólica:*\n\n"
        mensagem += noticias_eolica
    noticias_solar = retornar_noticias("database/noticias_solar.csv")
    if noticias_solar:
        mensagem += "☀️ *Últimas notícias sobre energia solar:*\n\n"
        mensagem += noticias_solar
    
    return mensagem

if __name__ == "__main__":
    print(criar_mensagem())