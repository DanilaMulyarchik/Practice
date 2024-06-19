from flask import Flask, request

app = Flask(__name__)

@app.route('/status')
def status():
    code = int(request.args.get('code', 200))
    return '', code


if __name__ == '__main__':
    app.run(debug=True)
