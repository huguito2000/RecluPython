from objetos.funciones import click_elemento, comboBox, text_elemento,scrollearElemento
from test.crearVacante.vacante_manual.paso4 import paso4
from objetos.crearVacante.vacanteManual.Obj_paso5 import psicometrica1, psicometrica2, psicometrica3, psicometrica4, \
    psicometrica5, psicometrica6, psicometrica7, psicometrica8, psicometrica9, psicometrica10, psicometrica11, \
    psicometrica12, psicometrica13, addpreguntaR1, preguntaR1, addpreguntaR2, preguntaR2, guardarR1, guardarR2, \
    siguiente

def paso5():
    try:
        carpeta = 'paso5'
        paso4 ()
        def psicometrias():

            click_elemento(psicometrica1, carpeta, 1)
            click_elemento(psicometrica2, carpeta, 1)
            click_elemento(psicometrica3, carpeta, 1)
            click_elemento(psicometrica4, carpeta, 1)
            click_elemento(psicometrica5, carpeta, 1)
            click_elemento(psicometrica6, carpeta, 1)
            click_elemento(psicometrica7, carpeta, 1)
            click_elemento(psicometrica8, carpeta, 1)
            click_elemento(psicometrica9, carpeta, 1)
            click_elemento(psicometrica10, carpeta, 1)
            click_elemento(psicometrica11, carpeta, 1)
            click_elemento(psicometrica12, carpeta, 1)
            click_elemento(psicometrica13, carpeta, 1)

        psicometrias()

        psicometrias()

        scrollearElemento(addpreguntaR1)
        click_elemento(addpreguntaR1, carpeta, 2)
        text_elemento(preguntaR1, 'pregunta 1', carpeta, 2)
        click_elemento(guardarR1, carpeta, 2)

        click_elemento(addpreguntaR2, carpeta, 2)
        text_elemento(preguntaR2, 'pregunta 2', carpeta, 2)
        click_elemento(guardarR2, carpeta, 2)

        click_elemento(siguiente,carpeta, 2)
        print("paso el paso 5")
        return 'paso el paso 5'

    except Exception as e:
        print('no paso el paso 5', str(e))
        return 'no paso el paso '
