import random
from test.Login import loginValido
from objetos.Obj_home import vacantes
from objetos.funciones import text_elemento, click_elemento, comboBox, captura_time, text_elemento_intro, \
    scrollearElemento
from objetos.crearVacante.vacanteManual.Obj_paso1 import crearVacante, manual, puesto, especialidad, numVacantes, \
    sueldoMensual, min, max, bonos, \
    bruto, neto, mostrarSueldo, beneficios, nomEmpresa, empresa, pais, estado, municipio, modalidad, siguiente


def p1():
    try:
        loginValido()
        carpeta = 'paso1'
        puestos = ['abogado', 'desarrollador', 'medico', 'contador', 'Filósofo', 'Profesor', 'Periodista', 'Enfermero']
        aleatorio = random.choice(puestos)

        click_elemento(vacantes, carpeta, 1)
        click_elemento(crearVacante, carpeta, 1)
        click_elemento(manual, carpeta, 1)
        text_elemento_intro(puesto, aleatorio, carpeta, 1)
        text_elemento(especialidad, 'automatizacion', carpeta, 1)

        comboBox(sueldoMensual, 2, carpeta, 1)
        text_elemento(min, '20000', carpeta, 1)
        text_elemento(max, '25000', carpeta, 1)
        click_elemento(bonos, carpeta, 1)
        click_elemento(bonos, carpeta, 1)
        click_elemento(bonos, carpeta, 1)
        scrollearElemento(bonos)

        click_elemento(bruto, carpeta, 1)
        click_elemento(neto, carpeta, 1)
        click_elemento(mostrarSueldo, carpeta, 1)

        click_elemento(beneficios, carpeta, 1)

        text_elemento_intro(nomEmpresa, 'involve', carpeta, 1)
        scrollearElemento(nomEmpresa)

        comboBox(pais, 1, carpeta, 1)
        comboBox(estado, 7, carpeta, 1)
        comboBox(municipio, 10, carpeta, 1)

        comboBox(modalidad, 1, carpeta, 1)

        click_elemento(siguiente, carpeta, 1)
        captura_time(carpeta, 1)

        print("se completo el primer paso")
        return "se cpmpleto el primer paso"
    except Exception as e:
        print("no se completo el primer paso", str(e))
        return "no se completo el primer paso"

