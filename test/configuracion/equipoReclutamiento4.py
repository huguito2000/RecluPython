import random
import time

from objetos.configuracion.Obj_empresa import perfil, cerrarSesion
from objetos.configuracion.obj_equipoReclu import reclutamiento, invitar, btn_invitar, email, cancelar
from objetos.Obj_home import Ajustes
from objetos.funciones import text_elemento, click_elemento
from test.Login import loginValido


def equipoReclu():
    try:
        loginValido()
        carpeta = 'equipoR eclu'
        num = random.randint(1, 100)
        click_elemento(Ajustes, carpeta, 2)
        click_elemento(reclutamiento, carpeta, 2)
        click_elemento(invitar, carpeta, 2)
        click_elemento(cancelar, carpeta, 2)
        click_elemento(cancelar, carpeta, 2)
        click_elemento(invitar, carpeta, 2)
        text_elemento(email, 'huguito.reclutador@yopmail.com', carpeta, 2)
        click_elemento(btn_invitar, carpeta, 2)
        time.sleep(2)
        text_elemento(email, 'huguito.reclutador' + str(num) + '@yopmail.com', carpeta, 2)
        click_elemento(btn_invitar, carpeta, 2)
        time.sleep(5)

        click_elemento(perfil, carpeta, 2)
        click_elemento(cerrarSesion, carpeta, 2)
        time.sleep(1)
        print('ya paso el equipo de reclutamiento')
        return 'ya paso el happy path'
    except Exception as e:
        print('No paso el equipo de reclutamiento')
        return 'No paso el equipo de reclutamiento'
