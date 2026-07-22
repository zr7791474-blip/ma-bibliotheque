import sqlite3
import os

def get_db_path():
    # Sur Vercel, l'environnement système est en lecture seule sauf le dossier /tmp
    if os.environ.get('VERCEL'):
        return '/tmp/bibliotheque.db'
    return 'bibliotheque.db'

def get_connection():
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT NOT NULL,
            auteur TEXT NOT NULL,
            prix REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Initialisation automatique au chargement
init_db()