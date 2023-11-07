import time
from test.registro.registro import correo
from objetos.browser import driver
from objetos.Obj_login import password, BtnContinuar, email
from objetos.registro.Obj_confirmacion import newCode, code, code1, code2, code3, code4, continuar, perfil, cerrarSesion
from objetos.registro.Obj_nombre import nombreR, apellidoP, empresa, sector, giro, continuarN
from objetos.funciones import click_elemento, text_elemento, captura_time, comboBox, codigo
from objetos.Obj_home import clientes, pausada, borrador, cerradas, activas, vacantes, \
    creditos, equipo, historial, tutorial, chat, Ajustes

contador = 0

carpeta = 'confirmacion'


def registroCompleto():
    try:
        captura_time(carpeta, 2)
        click_elemento(newCode, carpeta, 1)

        codigo(code, carpeta, code1, code2, code3, code4, 2)
        click_elemento(continuar, carpeta, 3)

        text_elemento(nombreR, 'Hugo', carpeta, 1)
        text_elemento(apellidoP, 'Rodriguez', carpeta, 1)
        text_elemento(empresa, 'involve', carpeta, 1)

        comboBox(sector, 11, carpeta, 1)
        comboBox(giro, 7, carpeta, 1)
        click_elemento(continuarN, carpeta, 3)
        print("se termino el registro")
        driver.refresh()
        time.sleep(3)
        text_elemento(email, correo, carpeta, 1)
        text_elemento(password, 'Abcd.1234', carpeta, 1)
        click_elemento(BtnContinuar, carpeta, 3)
        time.sleep(2)
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
        print("ya regrese a la pestaña principal")

        click_elemento(vacantes, carpeta, 3)
        click_elemento(perfil, carpeta, 2)
        click_elemento(cerrarSesion, carpeta, 2)
        time.sleep(2)
        print("se termino el registro completo")
        return "se termino el registro completo"
    except Exception as e:
        print("Error al pasar la confirmación", str(e))
        return "no se realizo el registro completo"
