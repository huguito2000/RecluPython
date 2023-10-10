import time
from test.registro import correo, registroValido
from objetos.browser import driver
from selenium.webdriver.common.by import By
from objetos.Obj_login import password, BtnContinuar, email
from objetos.registro.Obj_confirmacion import newCode, code, code1, code2, code3, code4, continuar
from objetos.registro.Obj_nombre import nombreR, apellidoP, empresa, sector, giro, continuarN
from objetos.funciones import click_elemento, text_elemento, captura_time, comboBox
from objetos.Obj_home import clientes, pausada, borrador, cerradas, activas, vacantes, \
    creditos, equipo, historial, tutorial, chat, Ajustes

contador = 0

carpeta = 'confirmacion'

def confirmacionValida():
    try:
        registroValido() # se manda a llamar a la clase de registro
        captura_time(carpeta, 2)
        click_elemento(newCode,carpeta, 1)

        Confirmacion = driver.find_element(By.XPATH, code)
        codigo = Confirmacion.text
        print(codigo.split(','))
        print(codigo[0])
        print(codigo[1])
        print(codigo[2])
        print(codigo[3])
        captura_time(carpeta, 2)
        text_elemento(code1, codigo[0], carpeta, 1)
        text_elemento(code2, codigo[1], carpeta, 1)
        text_elemento(code3, codigo[2], carpeta, 1)
        text_elemento(code4, codigo[3], carpeta, 1)
        click_elemento(continuar,carpeta, 3)

        text_elemento(nombreR, 'Hugo', carpeta, 1)
        text_elemento(apellidoP, 'Rodriguez', carpeta, 1)
        text_elemento(empresa, 'involve', carpeta, 1)

        comboBox(sector,11, carpeta,1)
        comboBox(giro, 7, carpeta, 1)
        click_elemento(continuarN, carpeta, 3)
        print("se termino el registro")
        driver.refresh()
        time.sleep(3)
        text_elemento(email, correo, carpeta, 1)
        text_elemento(password, 'Abcd.1234', carpeta, 1)
        click_elemento(BtnContinuar, carpeta, 3)
        time.sleep(10)
        print("ya se inicio session")

        click_elemento(pausada, carpeta, 1)
        click_elemento(borrador, carpeta, 1)
        click_elemento(cerradas, carpeta, 1)
        click_elemento(activas, carpeta, 2)
        print("paso el home")

        click_elemento(creditos, carpeta, 3)
        click_elemento(vacantes, carpeta, 3)
        click_elemento(equipo, carpeta, 3)
        click_elemento(clientes, carpeta, 3)
        click_elemento(historial, carpeta, 3)
        click_elemento(chat, carpeta, 3)
        click_elemento(chat, carpeta, 3)
        click_elemento(Ajustes, carpeta, 3)
        click_elemento(tutorial, carpeta, 3)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(5)
        click_elemento(vacantes, carpeta, 3)
        print("ya regrese a la pestaña principal")
        return "paso el menu"
    except Exception as e:
        print("Error al pasar la confirmación", str(e))
        return "Fallo los confirmación"

confirmacionValida()


