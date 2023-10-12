import random
import time
from objetos.configuracion.obj_equipoReclu import reclutamiento, invitar, btn_invitar, email, cancelar
from objetos.Obj_home import Ajustes
from objetos.funciones import text_elemento, click_elemento, captura_time


def equipoReclu():
    try:
        carpeta = 'equipoR eclu'
        num = random.randint(1,100)
        click_elemento(Ajustes,carpeta,2)
        click_elemento(reclutamiento,carpeta,2)
        click_elemento(invitar,carpeta,2)
        click_elemento(cancelar,carpeta,2)
        click_elemento(cancelar,carpeta,2)
        click_elemento(invitar,carpeta,2)
        text_elemento(email,'huguito.reclutador@yopmail.com',carpeta,2)
        click_elemento(btn_invitar,carpeta,2)
        time.sleep(2)
        text_elemento(email,'huguito.reclutador' + str(num) + '@yopmail.com',carpeta,2)
        click_elemento(btn_invitar,carpeta,2)
        time.sleep(1)
        print('ya paso el equipo de reclutamiento')
        return 'ya paso el equipo de reclutamiento'
    except Exception as e:
        print('No paso el equipo de reclutamiento')
        return 'No paso el equipo de reclutamiento'


