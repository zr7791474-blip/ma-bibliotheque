class Livre:
    def __init__(self, id=None, titre=None, auteur=None, prix=None):
        self.id = id
        self.titre = titre
        self.auteur = auteur
        self.prix = prix

    def __str__(self):
        return f"Livre(ID={self.id}, Titre=\"{self.titre}\", Auteur=\"{self.auteur}\", Prix={self.prix})"
