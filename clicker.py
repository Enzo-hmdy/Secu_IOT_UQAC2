# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 21:45:18 2023

@author: Antoine
"""

"""
Deux arguments pour lancer le script:
    1) view_number : nombre de fois où la machine va regarder le nombre de secondes minimales pour comptabiliser une vue
    2) link : lien de la vidéo ytb à "booster", si aucun lien mis ça sera une chanson mexicaine
"""

# =============================================================================
# from selenium_stealth import stealth
# =============================================================================
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# =============================================================================
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# =============================================================================
import sys
import time 
import random as rd

options = webdriver.FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

# =============================================================================
# stealth(driver,
#     languages = ["en-US", "en"],
#     vendor = "Google Inc.",
#     platform = "Win32",
#     webgl_vendor = "Intel Inc.",
#     renderer = "Intel Iris OpenGL Engine",
#     fix_hairline = False)
# =============================================================================


temps1 = 60 
temps2 = 90 
# pour donner un temps d'attente uniforme entre temps1 et temps2 
# car une vue youtube est comptabilisée après 30s
# mais il peut y avoir 30s de pubs unskippables


view_number = sys.argv[1]
try:
    link = sys.argv[2]
except:
    link = "https://www.youtube.com/watch?v=q-Rqdgna3Yw"


for _ in range(view_number):
    driver.get(link)
    time.sleep(5)
    video = driver.find_element(By.ID,'movie_player')
    video.send_keys(Keys.SPACE) 
    time.sleep(6)
    try:
        button = driver.find_element(By.CLASS_NAME,'ytp-ad-skip-button-container')
        button.click()
    except:
        pass
    time.sleep(rd.uniform(temps1,temps2))

driver.close()
driver.quit()
