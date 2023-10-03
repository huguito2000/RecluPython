from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import webdriver_manager.chrome
from datetime import datetime
import time
from objetos.Obj_login import email, password, BtnContinuar, mostrar, ocultar
import os


contador: int = 0

global driver
options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(webdriver_manager.chrome.ChromeDriverManager().install()), options=options)
driver.get("https://involveprereclu.involverh.com.mx/login")

def captura():
    global contador
    now = datetime.now()
    carpeta = '/Users/huguito/PycharmProjects/pythonProject/pythonProject/Reclutador/imagenes/login/' + str(now.day) + str(now.month)
    os.makedirs(carpeta, exist_ok=True)
    nombre = str(now.day) + str(now.month) + str(contador)
    captura_ruta = carpeta +'/'+ nombre+'.png'
    driver.save_screenshot(captura_ruta)
    print(captura_ruta)
    contador += 1


def login():
    time.sleep(2) # Let the user actually see something!
    campo_email = driver.find_element(By.XPATH, email)
    campo_email.send_keys('hug')
    captura()
    time.sleep(1)
    campo_email.clear()
    campo_email.send_keys('huguitoyopmail.com')
    captura()
    time.sleep(1)
    campo_email.clear()
    campo_email.send_keys('huguito.reclutador@yopmail.com')
    captura()
    time.sleep(1)
    campo_password = driver.find_element(By.XPATH, password)
    campo_password.send_keys('abcd.1234')
    captura()
    time.sleep(1)
    Mostrar = driver.find_element(By.XPATH, mostrar)
    Mostrar.click()
    captura()
    time.sleep(1)
    Ocultar = driver.find_element(By.XPATH, ocultar)
    Ocultar.click()
    time.sleep(1)
    captura()
    BtnLogin = driver.find_element(By.XPATH, BtnContinuar)
    BtnLogin.click()
    captura()
    time.sleep(1)
    campo_password = driver.find_element(By.XPATH, password)
    campo_password.send_keys('Abcd.1234')
    captura()
    time.sleep(1)
    Mostrar = driver.find_element(By.XPATH, mostrar)
    Mostrar.click()
    captura()
    time.sleep(1)
    Ocultar = driver.find_element(By.XPATH, ocultar)
    Ocultar.click()
    captura()
    time.sleep(1)
    BtnLogin = driver.find_element(By.XPATH, BtnContinuar)
    BtnLogin.click()
    time.sleep(1)
    captura()









