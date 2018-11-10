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
def json_result_content():
    JSON_RESULT_CONTENT = [
        {
            "text": "Calendário de Matrícula 1º/2019",
            "path": "/images/stories/documentos/calendarios/graduacao/cal_matricula/mat___2019_1.pdf",
            "url": "http://www.saa.unb.br/images/stories/documentos/calendarios/graduacao/cal_matricula/mat___2019_1.pdf"
        },
        {
            "text": "Calendário de Matrícula 2º/2018",
            "path": "/images/stories/documentos/calendarios/graduacao/cal_matricula/\tcal_2018_2.pdf",
            "url": "http://www.saa.unb.br/images/stories/documentos/calendarios/graduacao/cal_matricula/%09cal_2018_2.pdf"
        },
        {
            "text": "Calendário de Matrícula 1º/2018",
            "path": "/images/stories/documentos/calendarios/graduacao/cal_matricula/cal_de_matricula_em_disciplina_12018.pdf",
            "url": "http://www.saa.unb.br/images/stories/documentos/calendarios/graduacao/cal_matricula/cal_de_matricula_em_disciplina_12018.pdf"
        },
        {
            "text": "Calendário de Matrícula 2º/2017",
            "path": "/images/stories/documentos/calendarios/graduacao/cal_matricula/cal_matricula_22017.pdf",
            "url": "http://www.saa.unb.br/images/stories/documentos/calendarios/graduacao/cal_matricula/cal_matricula_22017.pdf"
        },
        {
            "text": "Calendário de Matrícula 1º/2017",
            "path": "/images/stories/documentos/calendarios/graduacao/cal_aluno/Cartaz_Calendario_Academico_1_2017.pdf",
            "url": "http://www.saa.unb.br/images/stories/documentos/calendarios/graduacao/cal_aluno/Cartaz_Calendario_Academico_1_2017.pdf"
        }
    ]

    return JSON_RESULT_CONTENT
