import subprocess
import os
from flask import Flask, send_file, jsonify
from scraper import PdfReader

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

OUTPUT_PATH = './outputs/'


@app.route('/')
def hello():
    return """
        <h1>WebCrawler - Registration</h1>
    """


@app.route('/registration/downloadPdf')
def downloadPdf():
    subprocess.check_output(['python', 'scraper.py'])
    pdf = PdfReader()
    file_name = pdf.downloadRegistration()
    image_name = f'{OUTPUT_PATH}{file_name}.png'
    if(os.path.isfile(image_name)):
        return send_file(image_name)
    else:
        return jsonify({
            'status': 'error',
            'description': 'pdf not found'
        }), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
