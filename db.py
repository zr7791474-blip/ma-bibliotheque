import mysql.connector

class DB:
    @staticmethod
    def get_connection():
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",     
                password="0000",   
                database="bibliotheque"
            )
            return conn
        except mysql.connector.Error as e:
            print(f"Erreur dial l'connexion: {e}")
            return None
