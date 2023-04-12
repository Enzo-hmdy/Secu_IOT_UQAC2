# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 00:28:18 2023

@author: Antoine
"""

import os
import zipfile
import requests
from io import BytesIO
from selenium import webdriver

# Définir le lien de téléchargement pour la dernière version de chromedriver
chromedriver_url = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"

# Récupérer la version la plus récente de chromedriver à partir du lien
version = requests.get(chromedriver_url).text.strip()

# Définir le lien de téléchargement pour la version de chromedriver spécifiée
chromedriver_download_url = f"https://chromedriver.storage.googleapis.com/{version}/chromedriver_win32.zip"

# Définir le nom du dossier où sera extrait chromedriver
chromedriver_folder = "chromedriver"

# Télécharger le fichier zip de chromedriver à partir du lien
response = requests.get(chromedriver_download_url)
zip_file = zipfile.ZipFile(BytesIO(response.content))

# Extraire chromedriver dans le dossier chromedriver
zip_file.extractall(chromedriver_folder)

# Ajouter le chemin du dossier chromedriver à la variable PATH de l'utilisateur
chromedriver_path = os.path.abspath(os.path.join(os.getcwd(), chromedriver_folder))
os.environ["PATH"] += os.pathsep + chromedriver_path