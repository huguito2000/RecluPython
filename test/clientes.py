from selenium.webdriver.common.by import By
from datetime import datetime
import time
import os
from objetos.Obj_home import vacantes
from objetos.browser import driver
from test.Login import loginValido
from selenium.webdriver.support.ui import Select
from objetos.Obj_clientes import clientes, nuevo, cerrar, nombreCliente, sector, giro, tipoEmpresa, cantidad1a10, \
    cantidad11a50, cantidad51a250, cantidad250, guardar, hambuguesa, eliminar, cancelar, eliminar2

contador: int = 0
def captura():
    global contador
    now = datetime.now()
    carpeta = '/Users/huguito/PycharmProjects/pythonProject/pythonProject/Reclutador/imagenes/clientes/' + str(
        now.day) + str(now.month)
    os.makedirs(carpeta, exist_ok=True)
    nombre = str(now.day) + str(now.month) + str(contador)
    captura_ruta = carpeta + '/' + nombre + '.png'
    driver.save_screenshot(captura_ruta)
    print(captura_ruta)
    contador += 1

loginValido()

Clientes = driver.find_element(By.XPATH, clientes)
Clientes.click()
captura()
time.sleep(3)

Clientes = driver.find_element(By.XPATH, nuevo)
Clientes.click()
captura()
time.sleep(1)

Clientes = driver.find_element(By.XPATH, cerrar)
Clientes.click()
captura()
time.sleep(1)

Clientes = driver.find_element(By.XPATH, nuevo)
Clientes.click()
captura()
time.sleep(1)

Clientes = driver.find_element(By.XPATH, nombreCliente)
Clientes.clear()
Clientes.send_keys('involver')
time.sleep(1)

Clientes = driver.find_element(By.XPATH, sector)
drop = Select(Clientes)
drop.select_by_index(11)
captura()
time.sleep(1)

Clientes = driver.find_element(By.XPATH, giro)
drop = Select(Clientes)
drop.select_by_index(7)
captura()
time.sleep(1)

Clientes = driver.find_element(By.XPATH, tipoEmpresa)
drop = Select(Clientes)
drop.select_by_index(1)
captura()
time.sleep(1)

Clientes = driver.find_element(By.XPATH, cantidad1a10)
Clientes.click()
captura()
time.sleep(1)

Clientes = driver.find_element(By.XPATH, cantidad11a50)
Clientes.click()
captura()
time.sleep(1)

Clientes = driver.find_element(By.XPATH, cantidad51a250)
Clientes.click()
captura()
time.sleep(1)

Clientes = driver.find_element(By.XPATH, cantidad250)
Clientes.click()
captura()
time.sleep(1)

Clientes = driver.find_element(By.XPATH, guardar)
Clientes.click()
captura()
time.sleep(1)

Clientes = driver.find_element(By.XPATH, hambuguesa)
Clientes.click()
captura()
time.sleep(1)

Clientes = driver.find_element(By.XPATH, eliminar)
Clientes.click()
captura()
time.sleep(1)

Clientes = driver.find_element(By.XPATH, cancelar)
Clientes.click()
captura()
time.sleep(2)

Clientes = driver.find_element(By.XPATH, hambuguesa)
Clientes.click()
captura()
time.sleep(1)

Clientes = driver.find_element(By.XPATH, eliminar)
Clientes.click()
captura()
time.sleep(1)

Clientes = driver.find_element(By.XPATH, eliminar2)
Clientes.click()
captura()
time.sleep(1)

Clientes = driver.find_element(By.XPATH, vacantes)
Clientes.click()
captura()
time.sleep(3)