import sys
import os

# Ajout du dossier racine au PATH Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

# Vercel utilise la variable 'app'
app = app