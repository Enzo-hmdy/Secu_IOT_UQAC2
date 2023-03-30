# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 17:20:20 2023

@author: Antoine
"""
"""
Deux arguments pour lancer le script:
    1) view_number : nombre de fois où la machine va regarder la page web
    2) link : lien de la page web à consulter
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

view_number = sys.argv[1]
link = sys.argv[2]

for _ in range(view_number):
    driver.get(link)
    time.sleep(5)

driver.close()
driver.quit()
