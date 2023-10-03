from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import webdriver_manager.chrome
from selenium.webdriver.common import keys
import time
from objetos.Obj_login import email, password, BtnContinuar
from objetos.Obj_home import clientes, pausada, borrador, cerradas, activas, vacantes, Btnperfil, configuracion, nombre, \
    apaterno, amaterno, subir, img_path, creditos, equipo, historial, tutorial, chat, Ajustes, eliminar, cancelar, \
    eliminar2


global driver
options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(webdriver_manager.chrome.ChromeDriverManager().install()), options=options)
driver.get("https://involveprereclu.involverh.com.mx/login")




def login():
    time.sleep(4) # Let the user actually see something!
    campo_email = driver.find_element(By.XPATH, email)
    campo_email.send_keys('huguito.reclutador@yopmail.com')
    time.sleep(1)
    campo_password = driver.find_element(By.XPATH, password)
    campo_password.send_keys('Abcd.1234')
    time.sleep(1)
    BtnLogin = driver.find_element(By.XPATH, BtnContinuar)
    BtnLogin.click()
    time.sleep(10)

def home():

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

def menu():
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




def perfil():
    BtnClientes = driver.find_element(By.XPATH, Btnperfil)
    BtnClientes.click()
    time.sleep(1)

    BtnClientes = driver.find_element(By.XPATH, configuracion)
    BtnClientes.click()
    time.sleep(1)

def ajustes():
    perfil()
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
    time.sleep(3)
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


