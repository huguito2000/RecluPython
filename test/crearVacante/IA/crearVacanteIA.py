import random
import time
from objetos.funciones import text_elemento, click_elemento, comboBox, text_elemento_intro
from test.Login import loginValido
from objetos.Obj_home import vacantes
from objetos.crearVacante.vacanteIA.paso1_IA import crearVacante, IA, puesto, personas_SI, personas_NO, \
    CantidadPersonas, Sueldo, SueldoIA, SueldoIA2, bruto, empresa, involve, pais, estado, municipio, modalidad, \
    siguiente1, siguiente, perfil, cerrarSesion, borrador


def vacanteIA():
    try:
        carpeta = 'crearVacanteIA'
        puestos = ['abogado', 'desarrollador', 'medico', 'contador', 'Filósofo', 'Profesor', 'Periodista', 'Enfermero']
        loginValido()
        aleatorio = random.choice(puestos)
        click_elemento(vacantes, carpeta, 2)
        click_elemento(crearVacante, carpeta, 2)
        click_elemento(IA, carpeta, 2)
        click_elemento(siguiente1, carpeta, 2)
        text_elemento_intro(puesto, aleatorio, carpeta, 2)
        time.sleep(1)
        click_elemento(personas_SI, carpeta, 2)
        click_elemento(personas_NO, carpeta, 2)
        click_elemento(personas_SI, carpeta, 2)
        text_elemento(CantidadPersonas, 2, carpeta, 2)
        comboBox(Sueldo, 2, carpeta, 2)
        time.sleep(2)
        click_elemento(SueldoIA, carpeta, 2)
        click_elemento(SueldoIA2, carpeta, 2)
        click_elemento(bruto, carpeta, 2)
        text_elemento(empresa, 'involve', carpeta, 2)
        click_elemento(involve, carpeta, 2)
        comboBox(pais, 1, carpeta, 2)
        comboBox(estado, 7, carpeta, 2)
        comboBox(municipio, 10, carpeta, 2)
        comboBox(modalidad, 1, carpeta, 2)
        click_elemento(siguiente, carpeta, 2)
        time.sleep(20)

        click_elemento(vacantes, carpeta, 2)
        click_elemento(borrador, carpeta, 2)
        time.sleep(3)
        click_elemento(perfil, carpeta, 2)
        click_elemento(cerrarSesion, carpeta, 2)
        time.sleep(2)

        print('se creo paso 1 de la vacante por IA')
        return 'se creo paso 1 de la vacante por IA'
    except Exception as e:
        print('no se creo paso 1 de la vacante por IA')
        return 'no se creo paso 1 de la vacante por IA'
