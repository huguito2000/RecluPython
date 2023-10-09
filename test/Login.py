from selenium.webdriver.common.by import By
from datetime import datetime
import time
import os
from objetos.Obj_login import email, password, BtnContinuar, mostrar, ocultar
from objetos.browser import driver

contador = 0

def captura():
    global contador
    now = datetime.now()
    carpeta = 'imagenes/login/' + str(now.day) + str(now.month)
    os.makedirs(carpeta, exist_ok=True)
    nombre = str(now.day) + str(now.month) + str(contador)
    captura_ruta = carpeta + '/' + nombre + '.png'
    driver.save_screenshot(captura_ruta)
    print(captura_ruta)
    contador += 1


def captura_time(segundos):
    time.sleep(segundos)
    captura()

def interactuar_con_campo(campo_xpath, valor, segundos=1):
    campo = driver.find_element(By.XPATH, campo_xpath)
    campo.send_keys(valor)
    captura_time(segundos)

def borrarText(xpath):
    campo = driver.find_element(By.XPATH, xpath)
    campo.clear()

def hacer_clic_en_elemento(elemento_xpath, segundos=1):
    elemento = driver.find_element(By.XPATH, elemento_xpath)
    elemento.click()
    captura_time(segundos)


def loginPrueba():
    try:
        interactuar_con_campo(email, 'hug', 1)
        borrarText(email)
        interactuar_con_campo(email, 'huguitoyopmail.com', 1)
        borrarText(email)
        interactuar_con_campo(email, 'huguito.reclutador@yopmail.com', 1)

        borrarText(email)

        interactuar_con_campo(password, 'abcd.1234', 1)
        hacer_clic_en_elemento(mostrar, 1)
        hacer_clic_en_elemento(ocultar, 1)
        borrarText(email)

        hacer_clic_en_elemento(BtnContinuar, 3)

        interactuar_con_campo(password, 'Abcd.1234', 1)
        hacer_clic_en_elemento(mostrar, 1)
        hacer_clic_en_elemento(ocultar, 1)

        hacer_clic_en_elemento(BtnContinuar, 10)

        print("Inicio de sesión exitoso")
        return "Inicio de sesión exitoso"
    except Exception as e:
        print("Error al iniciar sesión:", str(e))
        return "Fallo"


def loginValido():
    try:
        interactuar_con_campo(email, 'huguito.reclutador@yopmail.com', 1)
        interactuar_con_campo(password, 'Abcd.1234', 1)
        hacer_clic_en_elemento(BtnContinuar, 5)
        captura_time(2)
        print("Inicio de sesión exitoso")
        return "Inicio de sesión exitoso"
    except Exception as e:
        print("Error al iniciar sesión:", str(e))
        return "Fallo"



