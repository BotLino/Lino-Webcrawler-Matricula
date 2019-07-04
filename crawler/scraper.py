import pdfx
import os
import os.path
import time
import datetime
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from pdf2image import convert_from_path
import json

DOWNLOAD_PATH = './downloads/'
OUTPUT_PATH = './outputs/'


class TheCrawler():
    def __init__(self):
        self.process = CrawlerProcess(get_project_settings())

    def runCrawler(self):
        self.process.crawl('registration')
        self.process.start()


class JsonReader():
    def __init__(self):
        with open('result.json') as f:
            self.body = json.load(f)


class PdfReader():
    def __init__(self):
        self.data = JsonReader()

    def getCurrentPeriod(self):
        # gets current date and split year and month to get current period
        current_time_seconds = time.time()
        year_month = datetime.datetime.fromtimestamp(
            current_time_seconds).strftime('%Y-%m')
        year_month = year_month.split('-')
        year = year_month[0]
        month = int(year_month[1])
        if month >= 1 and month <= 6:
            semester = 1
        else:
            semester = 2

        masculine_ordinal_indicator = '\u00ba/'  # symbol º
        period = str(semester) + masculine_ordinal_separator + str(year)
        return period

    def convertsPdfToImage(self, file_name):
        if not(os.path.isfile(f'{OUTPUT_PATH}{pdfFileName}.png')):
            pdf = convert_from_path(f'{DOWNLOAD_PATH}{file_name}.pdf',  300)
            for page in pdf:
                page.save(f'{OUTPUT_PATH}{file_name}.png', 'PNG')

    def fixURL(url):
        tab_url_encoded = '%09'
        if tab_url_encoded in url:
            url = url.replace(tab_url_encoded, '')
        return url

    def downloadRegistration(self):
        # Downloads pdf from 'result.json'
        period = self.getCurrentPeriod()
        data = self.data
        if not os.path.exists(OUTPUT_PATH):
            os.mkdir(OUTPUT_PATH)

        for item in data.body:
            if period in item['text']:
                # fix url bug '%09'
                url = PdfReader.fixURL(item['url'])
                # sets filename
                file_name = url.split('/')
                file_name = file_name.pop()
                file_name = file_name.replace('.pdf', '')
                # download pdf
                if not(os.path.isfile(f'{DOWNLOAD_PATH}{file_name}.pdf')):
                    pdf = pdfx.PDFx(url)
                    pdf.download_pdfs(DOWNLOAD_PATH)

                return file_name


if __name__ == '__main__':
    crawl = TheCrawler()
    crawl.runCrawler()
    pdf = PdfReader()
    pdfFileName = pdf.downloadRegistration()
    pdf.convertsPdfToImage(pdfFileName)
