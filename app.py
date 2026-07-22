from flask import Flask, render_template, request, jsonify
from livre_dao import LivreDAO
from livre import Livre

app = Flask(__name__)

# --- ROUTES DE NAVIGATION ---
@app.route('/')
def index():
    return render_template('site.html')

# --- API REST (CRUD) ---
@app.route('/api/livres', methods=['GET'])
def api_get_livres():
    try:
        livres = LivreDAO.get_all()
        return jsonify({"success": True, "livres": [l.to_dict() for l in livres]}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@app.route('/api/livres/<int:id_livre>', methods=['GET'])
def api_get_livre(id_livre):
    livre = LivreDAO.get_by_id(id_livre)
    if livre:
        return jsonify({"success": True, "livre": livre.to_dict()}), 200
    return jsonify({"success": False, "message": "Livre non trouvé."}), 404

@app.route('/api/livres', methods=['POST'])
def api_add_livre():
    data = request.get_json() or {}
    titre = str(data.get('titre', '')).strip()
    auteur = str(data.get('auteur', '')).strip()
    prix_raw = data.get('prix')

    # Validation Côté Serveur
    if not titre:
        return jsonify({"success": False, "message": "Le titre est obligatoire."}), 400
    if not auteur:
        return jsonify({"success": False, "message": "L'auteur est obligatoire."}), 400
    
    try:
        prix = float(prix_raw)
        if prix < 0:
            return jsonify({"success": False, "message": "Le prix doit être un nombre positif."}), 400
    except (ValueError, TypeError):
        return jsonify({"success": False, "message": "Le prix doit être un nombre valide."}), 400

    nouveau_livre = Livre(titre=titre, auteur=auteur, prix=prix)
    livre_cree = LivreDAO.add(nouveau_livre)
    
    return jsonify({
        "success": True, 
        "message": "Livre ajouté avec succès !", 
        "livre": livre_cree.to_dict()
    }), 201

@app.route('/api/livres/<int:id_livre>', methods=['PUT'])
def api_update_livre(id_livre):
    livre_existant = LivreDAO.get_by_id(id_livre)
    if not livre_existant:
        return jsonify({"success": False, "message": "Livre introuvable."}), 404

    data = request.get_json() or {}
    titre = str(data.get('titre', '')).strip()
    auteur = str(data.get('auteur', '')).strip()
    prix_raw = data.get('prix')

    if not titre or not auteur:
        return jsonify({"success": False, "message": "Le titre et l'auteur sont obligatoires."}), 400

    try:
        prix = float(prix_raw)
        if prix < 0:
            return jsonify({"success": False, "message": "Le prix doit être positif."}), 400
    except (ValueError, TypeError):
        return jsonify({"success": False, "message": "Prix invalide."}), 400

    livre_existant.titre = titre
    livre_existant.auteur = auteur
    livre_existant.prix = prix

    if LivreDAO.update(livre_existant):
        return jsonify({"success": True, "message": "Livre mis à jour avec succès !", "livre": livre_existant.to_dict()}), 200
    return jsonify({"success": False, "message": "Erreur lors de la mise à jour."}), 500

@app.route('/api/livres/<int:id_livre>', methods=['DELETE'])
def api_delete_livre(id_livre):
    if LivreDAO.delete(id_livre):
        return jsonify({"success": True, "message": "Livre supprimé avec succès !"}), 200
    return jsonify({"success": False, "message": "Impossible de supprimer ce livre."}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)