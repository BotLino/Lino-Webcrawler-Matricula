import pdfx
import json
import os
import time
import datetime
from tabula import convert_into
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

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
    def downloadRegistration(self,period):
        #Downloads pdf from 'result.json'
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
                fileName = 'cal_2018_2'
                convert_into(
                    f'{DOWNLOAD_PATH}{fileName}.pdf',
                    f'{OUTPUT_PATH}{fileName}.tsv',
                    output_format='tsv')

crawl = TheCrawler()
crawl.runCrawler()
pdf = PdfReader()
pdf.downloadRegistration(period)

