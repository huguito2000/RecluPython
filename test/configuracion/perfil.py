import datetime
import os
import time
from selenium.webdriver.common.by import By
from test.Login import loginValido
from objetos.browser import driver
from datetime import datetime
from objetos.configuracion.Obj_perfil import Ajustes, nombre, apaterno, amaterno, img_path, subir, eliminar, cancelar, \
    eliminar2, cambiarPass, passAnterior, newPass, confirmarPassword, cambiarPassword, mostrarPass1, mostrarPass2, \
    mostrarPass3, telefonoCambio, newTelefono, cancelarTelefono, cambiarTelefono, cambiarEmail, newEmail, newEmail2, \
    passEmail, cancelarEmail, continuarEmail, mostrarEmail

contador: int = 0
password ='abcd.1234'


def captura():
    global contador
    now = datetime.now()
    carpeta = '/Users/huguito/PycharmProjects/pythonProject/pythonProject/Reclutador/imagenes/configuracion/perfil/' + str(
        now.day) + str(now.month)
    os.makedirs(carpeta, exist_ok=True)
    nombre = str(now.day) + str(now.month) + str(contador)
    captura_ruta = carpeta + '/' + nombre + '.png'
    driver.save_screenshot(captura_ruta)
    print(captura_ruta)
    contador += 1

def cambioPassword():
    global password
    perfil = driver.find_element(By.XPATH, passAnterior)
    perfil.clear()
    perfil.send_keys(password)
    captura()
    time.sleep(3)

    perfil = driver.find_element(By.XPATH, mostrarPass1)
    perfil.click()
    captura()
    time.sleep(3)

    perfil = driver.find_element(By.XPATH, newPass)
    perfil.clear()
    perfil.send_keys('Abcd.1234')
    captura()
    time.sleep(3)

    perfil = driver.find_element(By.XPATH, mostrarPass2)
    perfil.click()
    captura()
    time.sleep(3)

    perfil = driver.find_element(By.XPATH, confirmarPassword)
    perfil.clear()
    perfil.send_keys('Abcd.1234')
    captura()
    time.sleep(3)

    perfil = driver.find_element(By.XPATH, mostrarPass3)
    perfil.click()
    captura()
    time.sleep(3)

    perfil = driver.find_element(By.XPATH, cambiarPassword)
    perfil.click()
    captura()
    time.sleep(3)

captura()

loginValido()

captura()
perfil = driver.find_element(By.XPATH, Ajustes)
perfil.click()
captura()
time.sleep(3)

perfil = driver.find_element(By.XPATH, nombre)
perfil.clear()
perfil.send_keys('huguito')
captura()
time.sleep(1)

perfil = driver.find_element(By.XPATH, apaterno)
perfil.clear()
perfil.send_keys('rodriguez')
captura()
time.sleep(1)

perfil = driver.find_element(By.XPATH, amaterno)
perfil.clear()
perfil.send_keys('olivera')
captura()
time.sleep(1)

perfil= driver.find_element(By.XPATH, subir)
perfil.send_keys(img_path)
captura()
time.sleep(5)

perfil = driver.find_element(By.XPATH, eliminar)
perfil.click()
captura()
time.sleep(3)

perfil = driver.find_element(By.XPATH, cancelar)
perfil.click()
captura()
time.sleep(3)

perfil = driver.find_element(By.XPATH, eliminar)
perfil.click()
captura()
time.sleep(3)

perfil = driver.find_element(By.XPATH, eliminar2)
perfil.click()
captura()
time.sleep(3)

perfil = driver.find_element(By.XPATH, subir)
perfil.send_keys(img_path)
captura()
time.sleep(3)

perfil = driver.find_element(By.XPATH, cambiarPass)
perfil.click()
captura()
time.sleep(3)

cambioPassword()

password = 'Abcd.1234'

cambioPassword()

captura()

loginValido()


captura()
perfil = driver.find_element(By.XPATH, Ajustes)
perfil.click()
captura()
time.sleep(3)

perfil = driver.find_element(By.XPATH, telefonoCambio)
perfil.click()
captura()
time.sleep(3)

perfil = driver.find_element(By.XPATH, cancelarTelefono)
perfil.click()
captura()
time.sleep(3)

perfil = driver.find_element(By.XPATH, telefonoCambio)
perfil.click()
captura()
time.sleep(3)

perfil = driver.find_element(By.XPATH, newTelefono)
perfil.clear()
perfil.send_keys('5569777077')
captura()
time.sleep(1)

perfil = driver.find_element(By.XPATH, cambiarTelefono)
perfil.click()
captura()
time.sleep(3)


perfil = driver.find_element(By.XPATH, cambiarEmail)
perfil.click()
captura()
time.sleep(3)

perfil = driver.find_element(By.XPATH, cancelarEmail)
perfil.click()
captura()
time.sleep(3)

perfil = driver.find_element(By.XPATH, cambiarEmail)
perfil.click()
captura()
time.sleep(3)

perfil = driver.find_element(By.XPATH, newEmail)
perfil.clear()
perfil.send_keys('hugo')
captura()
time.sleep(1)
perfil.clear()
perfil.send_keys('hugoreclutador@yopmail.com')
captura()
time.sleep(3)

perfil = driver.find_element(By.XPATH, newEmail2)
perfil.clear()
perfil.send_keys('hugo')
captura()
time.sleep(1)
perfil.clear()
perfil.send_keys('hugoreclutador@yopmail.com')
captura()
time.sleep(3)

perfil = driver.find_element(By.XPATH, passEmail)
perfil.clear()
perfil.send_keys('abcd.1234')
captura()
time.sleep(1)

perfil = driver.find_element(By.XPATH, mostrarEmail)
perfil.click()
captura()
time.sleep(3)

perfil = driver.find_element(By.XPATH, continuarEmail)
perfil.click()
captura()
time.sleep(3)

perfil = driver.find_element(By.XPATH, passEmail)
perfil.clear()
perfil.send_keys('Abcd.1234')
captura()
time.sleep(3)

perfil = driver.find_element(By.XPATH, continuarEmail)
perfil.click()
captura()
time.sleep(3)

