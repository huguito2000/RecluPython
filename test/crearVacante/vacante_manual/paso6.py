import time
from objetos.browser import driver
from objetos.funciones import click_elemento
from objetos.crearVacante.vacanteManual.Obj_paso6 import siguiente, publicar
from test.crearVacante.vacante_manual.paso5 import paso5


def publicarVacante():
    try:
        carpeta = 'paso6'
        paso5()
        click_elemento(siguiente, carpeta, 2)
        click_elemento(publicar, carpeta, 2)
        time.sleep(3)
        driver.quit()
        print('paso el paso 6')
        return 'se publico correctamente la vacante'
    except Exception as e:
        print('no paso el paso 6', str(e))
        return 'no paso el paso 6'

publicarVacante()