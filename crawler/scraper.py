import pdfx
import json
import os
import time
import datetime
from tabula import convert_into
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from pdf2image import convert_from_path

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
        #gets current date and split year and month to get current period
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m')
        st = st.split('-')
        year = st[0]
        month = int(st[1])
        if month >= 1 and month <=6:
            semester = 1
        else:
            semester = 2
        
        period = str(semester) + '\u00ba/' + str(year)
        return period

    def downloadRegistration(self):
        #Downloads pdf from 'result.json'
        period = self.getCurrentPeriod()
        data = self.data
        if not os.path.exists(OUTPUT_PATH):
            os.mkdir(OUTPUT_PATH)

        for item in data.body:
            if "%09" in item['url']:
                url = item['url'].replace("%09","")
            else:
                url = item['url']
            
            if period in item['text']:
                pdf = pdfx.PDFx(url)
                pdf.download_pdfs(DOWNLOAD_PATH)
                fileName = url.split('/')
                fileName = fileName.pop()
                fileName = fileName.replace('.pdf','')
                pdf = convert_from_path(f'{DOWNLOAD_PATH}{fileName}.pdf', 300)
                for page in pdf:
                    page.save(f'{OUTPUT_PATH}{fileName}.png', 'PNG')

if __name__ == '__main__':
    crawl = TheCrawler()
    crawl.runCrawler()
    pdf = PdfReader()
    pdf.downloadRegistration()

