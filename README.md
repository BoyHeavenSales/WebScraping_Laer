# WebScraping_Laer
Projeto destinado á liga de energias renováveis. 

# Objetivo

Automatizar diariamente o envio das principais notícias sobre energias renováveis

# Etapa 1 — Fundamentos

## Objetivos

- [ ] Criar o repositório
- [ ] Criar ambiente virtual
- [ ] Instalar dependências
- [ ] Organizar a estrutura do projeto


## Estrutura das Pastas

### `scraper/`
Responsável pela coleta de informações. Todos os dados coletados são padronizados antes de serem enviados para as próximas etapas do sistema.


### `whatsapp/`
Responsável pela automação do WhatsApp. Contém as funções que abrem o navegador, realizam o login (quando necessário), localizam o grupo da Liga e enviam as mensagens.


### `database/`
Gerencia o armazenamento de dados do projeto. Armazena informações como notícias já enviadas, histórico de execuções e configurações, evitando o envio de conteúdo duplicado e permitindo consultas futuras.


# Etapa 2 — Buscar notícias

## Objetivos

Aprender:

- Requests
- BeautifulSoup

Criar funções para:

```
buscar_canal_solar()

buscar_portal_solar()

buscar_pv_magazine()

buscar_absolar()
```

Cada função deverá retornar:

```python
[
    [
        "titulo",
        "data",
        "hora", # Opcional
        "link",
    ]
]
```

# Etapa 3 — Organizar as notícias

Objetivos:

- remover duplicadas
- ordenar por data
- limitar quantidade