import json
import os
import subprocess
from flask import Flask, jsonify, redirect, url_for

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def hello():
    return """
        <h1>WebCrawler - Matricula</h1>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

    

    