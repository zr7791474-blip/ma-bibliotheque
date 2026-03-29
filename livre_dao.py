from db import DB 
from livre import Livre 

class LivreDAO: 

    def ajouter(self, livre): 
        conn = DB.get_connection() 
        if conn: 
            cursor = conn.cursor() 
            try: 
                sql = "INSERT INTO livre (titre, auteur, prix) VALUES (%s, %s, %s)" 
                val = (livre.titre, livre.auteur, livre.prix) 
                cursor.execute(sql, val) 
                conn.commit() 
            except Exception as e: 
                print(f"Erreur lors de l'ajout : {e}") 
                conn.rollback() 
            finally: 
                cursor.close() 
                conn.close() 

    def afficher(self): 
        conn = DB.get_connection() 
        livres = []
        if conn:
            cursor = conn.cursor() 
            cursor.execute("SELECT * FROM livre") 
            rows = cursor.fetchall() 
            for row in rows: 
                livres.append(Livre(row[0], row[1], row[2], row[3])) 
            conn.close() 
        return livres 

    def supprimer(self, id): 
        conn = DB.get_connection() 
        if conn: 
            cursor = conn.cursor() 
            try: 
                sql = "DELETE FROM livre WHERE id = %s" 
                cursor.execute(sql, (id,)) 
                conn.commit() 
            except Exception as e: 
                print(f"Erreur lors de la suppression : {e}") 
                conn.rollback() 
            finally: 
                cursor.close() 
                conn.close()
