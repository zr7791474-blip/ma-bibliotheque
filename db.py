import os
import psycopg2

class DB:
    @staticmethod
    def get_connection():
        # Vercel gha y-welli y-akhod DATABASE_URL mn l-environment variables
        db_url = os.environ.get('DATABASE_URL')
        try:
            conn = psycopg2.connect(db_url)
            return conn
        except Exception as e:
            print(f"Erreur dial l'connexion: {e}")
            return None
