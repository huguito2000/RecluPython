import time
from objetos.registro.Obj_confirmacion import newCode, code, code1, code2, code3, code4, continuar
from test import registro
from test.registro import driver
from selenium.webdriver.common.by import By
from datetime import datetime
import os
contador = 0

registro #se manda a llamar a la clase de registro

def captura():
    global contador
    now = datetime.now()
    carpeta = '/Users/huguito/PycharmProjects/pythonProject/pythonProject/Reclutador/imagenes/registro/confirmación/' + str(now.day) + str(now.month)
    os.makedirs(carpeta, exist_ok=True)
    nombre = str(now.day) + str(now.month) + str(contador)
    captura_ruta = carpeta +'/'+ nombre+'.png'
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






