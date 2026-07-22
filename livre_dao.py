from db import get_connection
from livre import Livre

class LivreDAO:
    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, titre, auteur, prix FROM livres ORDER BY id DESC")
        rows = cursor.fetchall()
        conn.close()
        return [Livre(row['id'], row['titre'], row['auteur'], row['prix']) for row in rows]

    @staticmethod
    def get_by_id(livre_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, titre, auteur, prix FROM livres WHERE id = ?", (livre_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Livre(row['id'], row['titre'], row['auteur'], row['prix'])
        return None

    @staticmethod
    def add(livre):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO livres (titre, auteur, prix) VALUES (?, ?, ?)", 
                       (livre.titre, livre.auteur, livre.prix))
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        livre.id = new_id
        return livre

    @staticmethod
    def update(livre):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE livres SET titre = ?, auteur = ?, prix = ? WHERE id = ?", 
                       (livre.titre, livre.auteur, livre.prix, livre.id))
        conn.commit()
        updated = cursor.rowcount > 0
        conn.close()
        return updated

    @staticmethod
    def delete(livre_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM livres WHERE id = ?", (livre_id,))
        conn.commit()
        deleted = cursor.rowcount > 0
        conn.close()
        return deleted