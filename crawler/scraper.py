import pdfx
import json
import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

period = "2\u00ba/2018"
bug = "%09"

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

crawl = TheCrawler()
crawl.runCrawler()
pdf = PdfReader()
pdf.downloadRegistration(period)

