import time
from test import registro
from test.registro import correo
from objetos.browser import driver
from selenium.webdriver.common.by import By
from datetime import datetime
import os
from objetos.Obj_login import password, BtnContinuar, email
from objetos.registro.Obj_confirmacion import newCode, code, code1, code2, code3, code4, continuar
from objetos.registro.Obj_nombre import nombreR, apellidoP, empresa, sector, giro, continuarN
from selenium.webdriver.support.ui import Select
from objetos.Obj_home import clientes, pausada, borrador, cerradas, activas, vacantes, Btnperfil, configuracion, nombre, \
    apaterno, amaterno, subir, img_path, creditos, equipo, historial, tutorial, chat, Ajustes, eliminar, cancelar, \
    eliminar2

contador = 0

registro  # se manda a llamar a la clase de registro


def captura():
    global contador
    now = datetime.now()
    carpeta = '/Users/huguito/PycharmProjects/pythonProject/pythonProject/Reclutador/imagenes/registro/confirmación/' + str(
        now.day) + str(now.month)
    os.makedirs(carpeta, exist_ok=True)
    nombre = str(now.day) + str(now.month) + str(contador)
    captura_ruta = carpeta + '/' + nombre + '.png'
    driver.save_screenshot(captura_ruta)
    print(captura_ruta)
    contador += 1


captura()
time.sleep(1)

Confirmacion = driver.find_element(By.XPATH, newCode)
Confirmacion.click()
captura()
time.sleep(1)

Confirmacion = driver.find_element(By.XPATH, code)
codigo = Confirmacion.text
print(codigo.split(','))
print(codigo[0])
print(codigo[1])
print(codigo[2])
print(codigo[3])
captura()
time.sleep(1)
Confirmacion = driver.find_element(By.XPATH, code1)
Confirmacion.send_keys(codigo[0])
captura()
time.sleep(1)

Confirmacion = driver.find_element(By.XPATH, code2)
Confirmacion.send_keys(codigo[1])
captura()
time.sleep(1)

Confirmacion = driver.find_element(By.XPATH, code3)
Confirmacion.send_keys(codigo[2])
captura()
time.sleep(1)

Confirmacion = driver.find_element(By.XPATH, code4)
Confirmacion.send_keys(codigo[3])
captura()
time.sleep(1)

Confirmacion = driver.find_element(By.XPATH, continuar)
Confirmacion.click()
captura()
time.sleep(3)

nombres = driver.find_element(By.XPATH, nombreR)
nombres.send_keys('hugo')
captura()
time.sleep(1)

nombres = driver.find_element(By.XPATH, apellidoP)
nombres.send_keys('hugo')
captura()
time.sleep(1)

nombres = driver.find_element(By.XPATH, empresa)
nombres.send_keys('involve')
captura()
time.sleep(1)

nombres = driver.find_element(By.XPATH, sector)
drop = Select(nombres)
drop.select_by_index(11)
captura()
time.sleep(1)

nombres = driver.find_element(By.XPATH, giro)
drop = Select(nombres)
drop.select_by_index(7)
captura()
time.sleep(1)

nombres = driver.find_element(By.XPATH, continuarN)
nombres.click()
captura()
time.sleep(3)

print("se termino el registro")

driver.refresh()
time.sleep(3)

campo_email = driver.find_element(By.XPATH, email)
campo_email.send_keys(correo)
captura()
time.sleep(1)
campo_password = driver.find_element(By.XPATH, password)
campo_password.clear()
campo_password.send_keys('Abcd.1234')
captura()
time.sleep(1)
BtnLogin = driver.find_element(By.XPATH, BtnContinuar)
BtnLogin.click()
time.sleep(10)
captura()
print("ya se inicio session")

Btnhome = driver.find_element(By.XPATH, pausada)
Btnhome.click()
time.sleep(1)

Btnhome = driver.find_element(By.XPATH, borrador)
Btnhome.click()
time.sleep(1)

Btnhome = driver.find_element(By.XPATH, cerradas)
Btnhome.click()
time.sleep(2)

Btnhome = driver.find_element(By.XPATH, activas)
Btnhome.click()
time.sleep(2)

menu = driver.find_element(By.XPATH, creditos)
menu.click()
time.sleep(3)

menu = driver.find_element(By.XPATH, vacantes)
menu.click()
time.sleep(3)

menu = driver.find_element(By.XPATH, equipo)
menu.click()
time.sleep(3)

menu = driver.find_element(By.XPATH, clientes)
menu.click()
time.sleep(3)

menu = driver.find_element(By.XPATH, historial)
menu.click()
time.sleep(3)

menu = driver.find_element(By.XPATH, chat)
menu.click()
time.sleep(3)

menu = driver.find_element(By.XPATH, chat)
menu.click()
time.sleep(3)

menu = driver.find_element(By.XPATH, Ajustes)
menu.click()
time.sleep(3)

menu = driver.find_element(By.XPATH, tutorial)
menu.click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)

menu = driver.find_element(By.XPATH, vacantes)
menu.click()
time.sleep(3)
print("ya pase a la pestaña principal")

BtnClientes = driver.find_element(By.XPATH, Btnperfil)
BtnClientes.click()
time.sleep(1)

BtnClientes = driver.find_element(By.XPATH, configuracion)
BtnClientes.click()
time.sleep(1)

CampoNombres = driver.find_element(By.XPATH, nombre)
CampoNombres.clear()
CampoNombres.send_keys('huguito')
time.sleep(1)
CampoNombres = driver.find_element(By.XPATH, apaterno)
CampoNombres.clear()
CampoNombres.send_keys('rodriguez')
time.sleep(1)
CampoNombres = driver.find_element(By.XPATH, amaterno)
CampoNombres.clear()
CampoNombres.send_keys('olivera')
time.sleep(1)
img_upload = driver.find_element(By.XPATH, subir)
img_upload.send_keys(img_path)
time.sleep(5)
img_upload = driver.find_element(By.XPATH, eliminar)
img_upload.click()
time.sleep(3)
img_upload = driver.find_element(By.XPATH, cancelar)
img_upload.click()
time.sleep(3)
img_upload = driver.find_element(By.XPATH, eliminar)
img_upload.click()
time.sleep(3)
img_upload = driver.find_element(By.XPATH, eliminar2)
img_upload.click()
time.sleep(3)
img_upload = driver.find_element(By.XPATH, subir)
img_upload.send_keys(img_path)
time.sleep(3)
