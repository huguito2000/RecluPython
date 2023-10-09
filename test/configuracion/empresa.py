import datetime
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from objetos.Obj_home import Ajustes
from test.Login import loginValido
from objetos.browser import driver
from datetime import datetime
from objetos.configuracion.Obj_empresa import (empresa, logo, eliminar, eliminar2, cancelar, nombreEmpresa, sector, giro,
tipoEmpresa, empleados1a10, empleados11a50, empleados50a250, empleados250, pais, cancelar2,actualizar, img_path)

contador: int = 0
def captura():
    global contador
    now = datetime.now()
    carpeta = '/Users/huguito/PycharmProjects/pythonProject/pythonProject/Reclutador/imagenes/configuracion/empresa/' + str(
        now.day) + str(now.month)
    os.makedirs(carpeta, exist_ok=True)
    nombre = str(now.day) + str(now.month) + str(contador)
    captura_ruta = carpeta + '/' + nombre + '.png'
    driver.save_screenshot(captura_ruta)
    print(captura_ruta)
    contador += 1
def captura_time(segundos):
    time.sleep(segundos)
    captura()


loginValido()

captura()
perfil = driver.find_element(By.XPATH, Ajustes)
perfil.click()
captura()
time.sleep(3)

perfil = driver.find_element(By.XPATH, empresa)
perfil.click()
captura()
time.sleep(3)

perfil = driver.find_element(By.XPATH, cancelar2)
perfil.click()
captura()
time.sleep(2)

perfil= driver.find_element(By.XPATH, logo)
perfil.send_keys(img_path)
captura()
driver.refresh()
time.sleep(5)

perfil = driver.find_element(By.XPATH, eliminar)
perfil.click()
captura()
time.sleep(2)

perfil = driver.find_element(By.XPATH, cancelar)
perfil.click()
captura()
time.sleep(1)

perfil = driver.find_element(By.XPATH, eliminar)
perfil.click()
captura()
time.sleep(2)

perfil = driver.find_element(By.XPATH, eliminar2)
perfil.click()
captura()
time.sleep(1)

perfil= driver.find_element(By.XPATH, logo)
perfil.send_keys(img_path)
captura()
driver.refresh()
time.sleep(3)

perfil = driver.find_element(By.XPATH, nombreEmpresa)
perfil.clear()
perfil.send_keys("involve")

perfil = driver.find_element(By.XPATH, sector)
drop = Select(perfil)
drop.select_by_index(11)
captura()
time.sleep(1)

perfil = driver.find_element(By.XPATH, giro)
drop = Select(perfil)
drop.select_by_index(7)
captura()
time.sleep(1)

perfil = driver.find_element(By.XPATH, tipoEmpresa)
drop = Select(perfil)
drop.select_by_index(1)
captura()
time.sleep(1)

perfil = driver.find_element(By.XPATH, empleados1a10)
perfil.click()
captura()
time.sleep(1)

perfil = driver.find_element(By.XPATH, empleados11a50)
perfil.click()
captura()
time.sleep(1)

perfil = driver.find_element(By.XPATH, empleados50a250)
perfil.click()
captura()
time.sleep(1)

perfil = driver.find_element(By.XPATH, empleados250)
perfil.click()
captura()
time.sleep(1)

perfil = driver.find_element(By.XPATH, actualizar)
perfil.click()
captura()
time.sleep(1)