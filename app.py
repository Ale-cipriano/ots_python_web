from flask import Flask, render_template

app = Flask("Meu App")

posts = [
    {
        "titulo": "Minha primeira postagem",
        "texto": "teste"
    },
    {
        "titulo": "Segunda postagem",
        "texto": "Outro teste"
    }
]

@app.route('/')
def exibir_entradas():
    entradas = posts  # Mock das entradas
    return render_template('exibir_entradas.html', entradas=entradas)