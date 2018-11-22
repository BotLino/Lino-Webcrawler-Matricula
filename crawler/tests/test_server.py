from freezegun import freeze_time
from scraper import PdfReader


class TestServer():

    @freeze_time('2018-11-09')
    def test_server_home(self, test_client, tmpdir):
        res = test_client.get('/')
        assert res.status_code == 200

    @freeze_time('2018-11-09')
    def test_get_image(self, test_client, json_result_content, tmpdir):
        res = test_client.get('/registration/downloadPdf')
        assert res.status_code == 200

    @freeze_time('2018-11-09')
    def test_get_semester(self, test_client, json_result_content, semester_period_result, tmpdir):
        res = test_client.get('registration/downloadPdf')

        pdf = PdfReader()
        period = pdf.getCurrentPeriod()

        assert semester_period_result == period
