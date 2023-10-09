import os
from datetime import datetime
from test.Login import loginValido
from objetos.browser import driver
from selenium.webdriver.common.by import By
import time
from objetos.Obj_home import clientes, pausada, borrador, cerradas, activas, vacantes, Btnperfil, configuracion, nombre, \
    apaterno, amaterno, subir, img_path, creditos, equipo, historial, tutorial, chat, Ajustes, eliminar, cancelar, \
    eliminar2

contador = 0
def captura():
    global contador
    now = datetime.now()
    carpeta = 'imagenes/home/' + str(now.day) + str(now.month)
    os.makedirs(carpeta, exist_ok=True)
    nombre = str(now.day) + str(now.month) + str(contador)
    captura_ruta = carpeta + '/' + nombre + '.png'
    driver.save_screenshot(captura_ruta)
    print(captura_ruta)
    contador += 1

def captura_time(segundos):
    time.sleep(segundos)
    captura()

def click_elemento(xpath, segundos = 1):
    Btnhome = driver.find_element(By.XPATH, xpath)
    Btnhome.click()
    captura_time(segundos)

def text_elemento(xpath, valor, segundos = 1):
    CampoNombres = driver.find_element(By.XPATH, xpath)
    CampoNombres.clear()
    CampoNombres.send_keys(valor)
    captura_time(segundos)

def cambio_imagen(xpath, valor, segundos = 2):
    perfil = driver.find_element(By.XPATH, xpath)
    perfil.send_keys(valor)
    time.sleep(segundos)
    captura_time(segundos)


def pasa_home():
    try:
        click_elemento(pausada, 1)
        click_elemento(borrador, 1)
        click_elemento(cerradas, 1)
        click_elemento(activas, 2)
        print("paso el home")
        return ("paso el home exitosamente")
    except Exception as e:
        print("Error en el home:", str(e))
        return "Fallo el home"
def menu():
    try:
        click_elemento(creditos, 3)
        click_elemento(vacantes, 3)
        click_elemento(equipo, 3)
        click_elemento(clientes, 3)
        click_elemento(historial, 3)
        click_elemento(chat, 3)
        click_elemento(chat, 3)
        click_elemento(Ajustes, 3)
        click_elemento(tutorial, 3)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(5)
        click_elemento(vacantes, 3)
        print("ya regrese a la pestaña principal")
        print("paso el menu")
        return ("paso el menu exitosamente")
    except Exception as e:
        print("Error al pasar el menu", str(e))
        return "Fallo el menu"

def perfil():
    try:
        click_elemento(Btnperfil, 1)
        click_elemento(configuracion, 1)
        print("paso el perfil")
        return "paso el perfil"
    except Exception as e:
        print("Error al pasar el perfil", str(e))
        return "Fallo el perfil"


def ajustes():
    try:
        text_elemento(nombre, 'huguito', 1)
        text_elemento(apaterno, 'rodriguez', 1)
        text_elemento(amaterno, 'olivera', 1)
        cambio_imagen(subir,img_path, 3)

        click_elemento(eliminar,3)
        click_elemento(cancelar, 3)
        click_elemento(eliminar, 3)
        click_elemento(eliminar2, 3)
        text_elemento(subir, img_path, 5)
        cambio_imagen(subir, img_path, 3)
        
        print("ya pasaron los ajustes")
        return "ya pasaron los ajustes"
    except Exception as e:
        print("Error al pasar los ajustes", str(e))
        return "Fallo los ajustes"




'''
loginValido()
pasa_home()
print("pase el home")
menu()
print("pase el menu")
perfil()
print("pase el perfil")
ajustes()
print("pase los ajustes")
'''






