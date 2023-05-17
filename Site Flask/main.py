from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/projetos/python")
def projetos_python():
    return render_template("projetos_python.html")

@app.route("/projetos/microcontrolador")
def projetos_microcontrolador():
    return render_template("projetos_micro.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")


if __name__ == "__main__":
    app.run(debug=True)
