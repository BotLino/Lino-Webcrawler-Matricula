from freezegun import freeze_time
import json
import pytest

class TestServer():

    @freeze_time('2018-11-09')
    def test_get_image(self,test_client,json_result_content, tmpdir):
        res = test_client.get('/registration/downloadPdf')
        assert res.status_code == 200