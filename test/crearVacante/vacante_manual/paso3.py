from objetos.funciones import click_elemento, comboBox, text_elemento_intro
from objetos.crearVacante.vacanteManual.Obj_paso3 import nivelEstudios, estatuAcademico, titulo, institucion, addTalento, area, administracion, \
    cancelar, agregar, hdura, addHduras, hBlandas, addHblandas, idioma, addIdioma, siguiente

def p3():
    try:
        carpeta = 'paso3'
        comboBox(nivelEstudios,6,carpeta,2,)
        comboBox(estatuAcademico,5,carpeta,2,)
        text_elemento_intro(titulo,'ingeniero',carpeta, 2)
        text_elemento_intro(institucion,'unam',carpeta, 2)

        click_elemento(addTalento,carpeta,2)
        comboBox(area,1,carpeta,2)
        click_elemento(administracion,carpeta,2)
        click_elemento(cancelar,carpeta,2)


        click_elemento(addTalento,carpeta,2)
        comboBox(area,1,carpeta,2)
        click_elemento(administracion,carpeta,2)
        click_elemento(agregar,carpeta,2)

        text_elemento_intro(hdura, 'excel', carpeta,2)
        click_elemento(addHduras, carpeta, 2)

        text_elemento_intro(hBlandas, 'trabajo en equipo', carpeta,2)
        click_elemento(addHblandas, carpeta, 2)

        comboBox(idioma,1, carpeta, 2)
        click_elemento(addIdioma, carpeta, 2)

        click_elemento(siguiente, carpeta, 2)
        print('paso el paso 3')
        return 'paso el paso 3'
    except Exception as e:
        print('no paso el paso3', str(e))
        return 'no paso el paso 3'


