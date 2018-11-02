import subprocess
from flask import Flask, send_file
from scraper import PdfReader

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def hello():
    return """
        <h1>WebCrawler - Registration</h1>
    """


@app.route('/registration/downloadPdf')
def downloadPdf():
    subprocess.check_output(['python', 'scraper.py'])
    pdf = PdfReader()
    fileName = pdf.downloadRegistration()
    fileName = f'outputs/{fileName}.png'

    return send_file(fileName)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
