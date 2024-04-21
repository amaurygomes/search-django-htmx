# Bem-vindo ao Searchag

## Introdução

**Searchag** é uma aplicação web desenvolvida para facilitar a busca por perguntas e respostas cadastradas. Este projeto foi criado com fins educativos e utiliza uma combinação de tecnologias modernas para proporcionar uma experiência interativa ao usuário.

Para mais projetos e informações, visite meu site: [amaurygomes.com.br](https://amaurygomes.com.br).

## Tecnologias Utilizadas

- **Django 5.0.3**: Framework web para desenvolvimento em Python.
- **HTMX**: Biblioteca que permite interações dinâmicas no lado do cliente, carregada via CDN.
- **AlpineJS**: Framework JavaScript leve, também utilizado via CDN.

## Como Instalar e Rodar o Projeto

### Pré-requisitos:

- Docker instalado em sua máquina.
- Git para clonar o repositório.

### Passo a Passo:

1. **Clone o repositório:**
    ```bash
    git clone https://github.com/amaurygomes/search-django-htmx.git
    ```

2. **Construa a imagem Docker:**
    ```bash
    docker build -t nome_da_imagem .
    ```

3. **Execute o contêiner:**
    ```bash
    docker run -d -p porta_host:porta_contêiner nome_da_imagem
    ```

## Acessando a Aplicação

- **Interface Web:** Acesse `localhost:porta_host` em seu navegador para interagir com a aplicação.
- **Painel Administrativo:** Acesse `localhost:porta_host/auth/login/` para gerenciar as perguntas e respostas.


## Importar csv para o sqlite

* O arquivo csv deve conter 2 colunas "Question" e "Correct Answer" para funcionar.

* Será implementado furturamente o upload do csv

* Por enquanto é nessecário executar manualmente, com o container já em execução.

* Lembre se de alterar nome do arquivo csv no export_csv_django.py  

>csv_file_path = 'redes_out.csv'

## Configurações Padrão:

- **Usuário:** admin
- **Senha:** changeme
- **E-mail:** admin@example.com

---

Este projeto é mantido por Amaury Gomes. Para contribuições e suporte, por favor, entre em contato através do site [amaurygomes.com.br](https://amaurygomes.com.br).

