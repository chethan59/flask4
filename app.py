from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from main import ok
app = Flask(__name__)


@app.route('/')
def hello_world():
    ok.me()
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=5000, debug=True)
    #app.debug = True
    #app.run(debug=True)
    app.run()