from flask import Flask, request, render_template, redirect
from livre_dao import LivreDAO
from livre import Livre

app = Flask(__name__)
dao = LivreDAO()

@app.route("/")
def home():
    livres = dao.afficher()
    return render_template("site.html", livres=livres)

@app.route("/add", methods=["POST"])
def add():
    titre = request.form["titre"]
    auteur = request.form["auteur"]
    prix = float(request.form["prix"])
    livre = Livre(None, titre, auteur, prix)
    dao.ajouter(livre)
    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    dao.supprimer(id)
    return redirect("/")

if __name__ == "__main__":
    # host="0.0.0.0" hiya l-mohimma bach t-telefoun yqder ydkhol
    app.run(host="0.0.0.0", port=5000, debug=True)
