from flask import Flask

app = Flask("Meu App")

@app.route('/')
def hello():
    return "<h1>Hello World</h1>"

@app.route('/novo')
def nova():
    return "<h1> Nova Pagina </h1>"
