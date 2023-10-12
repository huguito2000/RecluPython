import os
from datetime import datetime

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from objetos.browser import driver
import time
import random
from selenium.webdriver.support.ui import Select

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
    driver.implicitly_wait(2)
    Btnhome.click()
    captura_time(carpeta, segundos)

def text_elemento(xpath, valor,carpeta:str, segundos = 1):
    CampoNombres = driver.find_element(By.XPATH, xpath)
    driver.implicitly_wait(2)
    CampoNombres.clear()
    CampoNombres.send_keys(valor)
    captura_time(carpeta, segundos)

def text_elemento_intro(xpath, valor,carpeta:str, segundos = 1):
    CampoNombres = driver.find_element(By.XPATH, xpath)
    driver.implicitly_wait(2)
    CampoNombres.clear()
    CampoNombres.send_keys(valor)
    time.sleep(1)
    CampoNombres.send_keys(Keys.ENTER)
    captura_time(carpeta, segundos)

ruta = ''
def foto(xpath):
    global ruta
    imagen = random.randint(0,10)
    print(imagen)
    ruta = ('/Users/huguito/PycharmProjects/pythonProject/pythonProject/Reclutador/Archivos/' + str(imagen) +'.jpeg')
    print(ruta)
    return ruta


def cambio_imagen(xpath, valor, carpeta: str, segundos = 2):
    perfil = driver.find_element(By.XPATH, xpath)
    driver.implicitly_wait(2)
    perfil.send_keys(valor)
    time.sleep(segundos)
    captura_time(carpeta, segundos)

def comboBox(xpath, valor, carpeta:str,segundos = 2):
    nombres = driver.find_element(By.XPATH, xpath)
    driver.implicitly_wait(2)
    drop = Select(nombres)
    drop.select_by_index(valor)
    captura_time(carpeta, segundos)



