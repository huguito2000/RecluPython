import time
from objetos.funciones import click_elemento
from objetos.crearVacante.vacanteManual.Obj_paso6 import siguiente, publicar, cerrarSesion, perfil


def publicarVacante():
    try:
        carpeta = 'paso6'
        click_elemento(siguiente, carpeta, 2)
        click_elemento(publicar, carpeta, 2)
        time.sleep(6)
        click_elemento(perfil, carpeta, 2)
        click_elemento(cerrarSesion, carpeta, 2)
        time.sleep(2)
        print('paso el paso 6')
        return 'se publico correctamente la vacante'
    except Exception as e:
        print('no paso el paso 6', str(e))
        return 'no paso el paso 6'

