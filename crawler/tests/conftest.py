import pytest
from server import app


@pytest.fixture(scope='module')
def test_client():
    flask_app = app
    testing_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


@pytest.fixture
def semester_period_result():
    return '2\u00ba/2018'


@pytest.fixture
def json_corrupted():
    JSON_CORRUPTED = [
        {
            "text": "Calendário de Matrícula 1º/2019"
        },
        {
            "text": "Calendário de Matrícula 2º/2018"
        },
        {
            "text": "Calendário de Matrícula 1º/2018"
        },
        {
            "text": "Calendário de Matrícula 2º/2017"
        },
        {
            "text": "Calendário de Matrícula 1º/2017"
        }
    ]

    return JSON_CORRUPTED


@pytest.fixture
def json_result_content():
    SAA_ROUTE = '/images/stories/documentos/calendarios/graduacao/'
    SAA_URL = f'http://www.saa.unb.br{SAA_ROUTE}'
    CAL = 'cal_matricula/'
    PATH = '/images/stories/documentos/calendarios/graduacao'
    JSON_RESULT_CONTENT = [
        {
            "text": "Calendário de Matrícula 1º/2019",
            "path": f'{PATH}{CAL}mat___2019_1.pdf',
            "url": f'{SAA_URL}{CAL}mat___2019_1.pdf'
        },
        {
            "text": "Calendário de Matrícula 2º/2018",
            "path": f'{PATH}{CAL}\tcal_2018_2.pdf',
            "url": f'{SAA_URL}{CAL}%09cal_2018_2.pdf'
        },
        {
            "text": "Calendário de Matrícula 1º/2018",
            "path": f'{PATH}{CAL}cal_de_matricula_em_disciplina_12018.pdf',
            "url": f'{SAA_URL}{CAL}cal_de_matricula_em_disciplina_12018.pdf'
        },
        {
            "text": "Calendário de Matrícula 2º/2017",
            "path": f'{PATH}{CAL}cal_matricula_22017.pdf',
            "url": f'{SAA_URL}{CAL}cal_matricula_22017.pdf'
        },
        {
            "text": "Calendário de Matrícula 1º/2017",
            "path": f'{PATH}cal_aluno/Cartaz_Calendario_Academico_1_2017.pdf',
            "url": f'{SAA_URL}cal_aluno/Cartaz_Calendario_Academico_1_2017.pdf'
        }
    ]

    return JSON_RESULT_CONTENT
