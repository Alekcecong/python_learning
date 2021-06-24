
from flask import Flask,request

app = Flask(__name__,static_folder="static")

@app.route('/')
def index():
    return 'Hello World'


@app.route('/download_file')
def download():
    file_path = request.args.get('down_url', '')
    invaration_code = request.args.get('ivc', '')

    if not invaration_code == '1Css':
        return ''

    try:
        file = open(file_path)
        data = file.read()

        file.close()

        return data
    except:
        pass

    return '???'


if __name__ == '__main__':
    app.debug = False
    app.run('0.0.0.0',8000)
