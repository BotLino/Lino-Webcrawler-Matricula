# Lino-Webcrawler-Matricula
## Objetivo
Microsserviço responsável por obter os dados de período de matrícula e envia-los ao usuário de forma gráfica a partir de uma imagem.
## Como usar
### Pré requisitos
Instale o docker e o docker-compose, e rode o seguinte comando:
```
$ docker build --rm -t webcrawlermatricula .
```
Após o build:
```
$ docker run --rm -it -p 5000:5000 -v $PWD:/Lino-Webcrawler-Matricula webcrawlermatricula
```
### Endpoints
### ```/registration/downloadPdf```
Objetivo: Em sua primeira execução realiza o download do Pdf com o calendário de matrícula do site do **saa unb**, converte o PDF para PNG e retorna a imagem na Url em questão. Nas execuções subsequentes o download nem a conversão é realizada, apenas o envio da imagem na Url.

Verbo: ```GET```

| Parâmetros de entrada | Descrição |
| :-------------------: | :-------: |
| Nenhum                |
