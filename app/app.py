from flask import Flask

app = Flask(__name__)


@app.route('/')
def start():  # put application's code here
    return {"status": "start page"}


@app.route('/health/')
def health():  # put application's code here
    return {"status": "OK"}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
