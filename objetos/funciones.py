import os
from datetime import datetime
from selenium.webdriver.common.by import By
from objetos.browser import driver
import time

contador = 1
def captura(carpeta:str):
    global contador
    now = datetime.now()
    carpeta = 'imagenes/' + str(carpeta)+'/' + str(now.day) + str(now.month)
    os.makedirs(carpeta, exist_ok=True)
    nombre = str(now.day) + str(now.month) + str(contador)
    captura_ruta = carpeta + '/' + nombre + '.png'
    driver.save_screenshot(captura_ruta)
    print(captura_ruta)
    contador += 1
def captura_time(carpeta:str, segundos):
    time.sleep(segundos)
    captura(carpeta)

def click_elemento(xpath,carpeta:str, segundos = 1 ):
    Btnhome = driver.find_element(By.XPATH, xpath)
    Btnhome.click()
    captura_time(carpeta, segundos)

def text_elemento(xpath, valor,carpeta:str, segundos = 1):
    CampoNombres = driver.find_element(By.XPATH, xpath)
    CampoNombres.clear()
    CampoNombres.send_keys(valor)
    captura_time(carpeta, segundos)

def cambio_imagen(xpath, valor, carpeta: str, segundos = 2):
    perfil = driver.find_element(By.XPATH, xpath)
    perfil.send_keys(valor)
    time.sleep(segundos)
    captura_time(carpeta, segundos)