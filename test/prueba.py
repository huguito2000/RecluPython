from test import Login
from test.Login import driver
from selenium.webdriver.common.by import By
import time
from objetos.Obj_home import clientes, pausada, borrador, cerradas, activas, vacantes, Btnperfil, configuracion, nombre, \
    apaterno, amaterno, subir, img_path, creditos, equipo, historial, tutorial, chat, Ajustes, eliminar, cancelar, \
    eliminar2


Login

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

