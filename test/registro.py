from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import webdriver_manager.chrome
from datetime import datetime
import time
import os
from objetos.registro.Obj_email import crearCuenta, email, telefono, password, mostrar1, ocultar1, password2, mostrar2, \
    ocultar2, TyC, cerrar, AvisosPrivacidad, cookies, legales, continuar

global driver
options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(webdriver_manager.chrome.ChromeDriverManager().install()), options=options)
driver.get("https://involveprereclu.involverh.com.mx/login")

contador: int = 0

now = datetime.now()
correo = 'reclu'+ str(now.day) + str(now.month) + str(now.minute) + str(now.second) + '@yopmail.com'
print(correo)

def captura():
    global contador
    now = datetime.now()
    carpeta = '/Users/huguito/PycharmProjects/pythonProject/pythonProject/Reclutador/imagenes/registro/registro/' + str(now.day) + str(now.month)
    os.makedirs(carpeta, exist_ok=True)
    nombre = str(now.day) + str(now.month) + str(contador)
    captura_ruta = carpeta +'/'+ nombre+'.png'
    driver.save_screenshot(captura_ruta)
    print(captura_ruta)
    contador += 1

def registro():
    time.sleep(2)
    CrearCuenta = driver.find_element(By.XPATH, crearCuenta)
    CrearCuenta.click()
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, email)
    CrearCuenta.send_keys('reclutador')
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, telefono)
    CrearCuenta.send_keys('5569777077')
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, password)
    CrearCuenta.send_keys('abcd.1234')
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, mostrar1)
    CrearCuenta.click()
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, ocultar1)
    CrearCuenta.click()
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, password2)
    CrearCuenta.send_keys('abcd.1234')
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, mostrar2)
    CrearCuenta.click()
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, ocultar2)
    CrearCuenta.click()
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, TyC)
    CrearCuenta.click()
    captura()
    time.sleep(2)

    CrearCuenta = driver.find_element(By.XPATH, cerrar)
    CrearCuenta.click()
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, AvisosPrivacidad)
    CrearCuenta.click()
    captura()
    time.sleep(2)

    CrearCuenta = driver.find_element(By.XPATH, cerrar)
    CrearCuenta.click()
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, AvisosPrivacidad)
    CrearCuenta.click()
    captura()
    time.sleep(2)

    CrearCuenta = driver.find_element(By.XPATH, cerrar)
    CrearCuenta.click()
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, cookies)
    CrearCuenta.click()
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, cerrar)
    CrearCuenta.click()
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, legales)
    CrearCuenta.click()
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, legales)
    CrearCuenta.click()
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, continuar)
    CrearCuenta.click()
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, email)
    CrearCuenta.clear()
    CrearCuenta.send_keys('reclutador')
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, continuar)
    CrearCuenta.click()
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, email)
    CrearCuenta.clear()
    CrearCuenta.send_keys('reclutador@yopmail.com')
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, continuar)
    CrearCuenta.click()
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, email)
    CrearCuenta.clear()
    CrearCuenta.send_keys('reclutadoryopmail.com')
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, continuar)
    CrearCuenta.click()
    captura()
    time.sleep(1)

def registroValido():
    time.sleep(2)
    CrearCuenta = driver.find_element(By.XPATH, crearCuenta)
    CrearCuenta.click()
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, email)
    CrearCuenta.clear()
    CrearCuenta.send_keys(correo)
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, telefono)
    CrearCuenta.send_keys('5569777077')
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, legales)
    CrearCuenta.click()
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, password)
    CrearCuenta.clear()
    CrearCuenta.send_keys('Abcd.1234')
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, mostrar1)
    CrearCuenta.click()
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, ocultar1)
    CrearCuenta.click()
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, password2)
    CrearCuenta.clear()
    CrearCuenta.send_keys('Abcd.1234')
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, mostrar2)
    CrearCuenta.click()
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, ocultar2)
    CrearCuenta.click()
    captura()
    time.sleep(1)

    CrearCuenta = driver.find_element(By.XPATH, continuar)
    CrearCuenta.click()
    captura()
    time.sleep(3)
    print("ya se hizo el registro")
registroValido()

time.sleep(1)

