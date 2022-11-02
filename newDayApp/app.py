from flask import Flask

app = Flask(__name__)

@app.route('/homepage')
def helloIndex():
    return 'Hello New Day!'

app.run(host='0.0.0.0', port=5000)
