import time

from objetos.Obj_login import email, password, BtnContinuar, mostrar, ocultar
from objetos.funciones import click_elemento, text_elemento, captura_time
carpeta = 'login'

def prueba():
    try:
        text_elemento(email, 'huguito.reclutador@yopmail.com', carpeta, 1)
        text_elemento(password, 'Abcd.1234', carpeta, 1)
        click_elemento(BtnContinuar, carpeta, 1)
        captura_time(carpeta, 2)
        time.sleep(2)
        print("Inicio de sesión exitoso")
        return "Inicio de sesión exitoso"
    except Exception as e:
        print("Error al iniciar sesión:", str(e))
        return "Fallo"

prueba()