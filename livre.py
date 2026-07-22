class Livre:
    def __init__(self, id_livre=None, titre="", auteur="", prix=0.0):
        self.id = id_livre
        self.titre = titre
        self.auteur = auteur
        self.prix = float(prix)

    def to_dict(self):
        return {
            "id": self.id,
            "titre": self.titre,
            "auteur": self.auteur,
            "prix": self.prix
        }