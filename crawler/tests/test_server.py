from freezegun import freeze_time
from pprint import pprint
import requests
import time
import datetime
import json

class TestServer():

    @freeze_time('2018-11-09')
    def test_get_image(self,test_client,json_result_content, tmpdir):
        res = test_client.get('/registration/downloadPdf')
        assert res.status_code == 200

    @freeze_time('2018-11-09')
    def test_json_link(self,test_client,json_result_content,tmpdir):
        res = test_client.get('/registration/downloadPdf')

        with open('result.json','r') as result_json:
            data = json.loads(result_json.read())
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m')
            st = st.split('-')
            year = st[0]
            month = int(st[1])
            if month >= 1 and month <= 6:
                semester = 1
            else:
                semester = 2

            period = str(semester) + '\u00ba/' + str(year)
            for item in data:
                if period in item['text']:
                    url = item['url']
                    if "%09" in url:
                        url = url.replace("%09", "")
                    res = requests.get(url)
                    assert res.status_code == 200

        pprint(data)