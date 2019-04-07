FROM python:3.6

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install default-jdk -y

RUN apt-get update && apt-get -y install poppler-utils

ADD . /Lino-Webcrawler-Matricula

WORKDIR /Lino-Webcrawler-Matricula

RUN pip install -r requirements.txt

WORKDIR /Lino-Webcrawler-Matricula/crawler

EXPOSE 5012

CMD python server.py
