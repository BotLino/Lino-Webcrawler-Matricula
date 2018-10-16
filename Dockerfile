FROM python:3.6

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install default-jdk -y

WORKDIR /Lino-Webcrawler-Matricula

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR /Lino-Webcrawler-Matricula/crawler

EXPOSE 5004

CMD sleep infinity