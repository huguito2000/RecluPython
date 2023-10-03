from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import webdriver_manager.chrome
from selenium.webdriver.common import keys
import time
from objetos.Obj_login import email, password, BtnContinuar
from objetos.Obj_home import clientes, pausada, borrador, cerradas, activas, vacantes, Btnperfil, configuracion, nombre, \
    apaterno, amaterno, subir, img_path, creditos, equipo, historial, tutorial, chat, Ajustes, eliminar, cancelar, \
    eliminar2
from test.Login import driver,login

def home():

    Btnhome = driver.find_element(By.XPATH, pausada)
    Btnhome.click()
    time.sleep(1)

    Btnhome = driver.find_element(By.XPATH,borrador)
    Btnhome.click()
    time.sleep(1)

    Btnhome = driver.find_element(By.XPATH, cerradas)
    Btnhome.click()
    time.sleep(2)

    Btnhome = driver.find_element(By.XPATH, activas)
    Btnhome.click()
    time.sleep(2)

login()

home()