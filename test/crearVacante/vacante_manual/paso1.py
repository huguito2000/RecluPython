import random
from test.Login import loginValido
from objetos.Obj_home import vacantes
from objetos.funciones import text_elemento, click_elemento, comboBox, captura_time,text_elemento_intro, scrollearElemento
from objetos.crearVacante.vacanteManual.paso_1 import crearVacante, manual, puesto, especialidad, numVacantes, sueldoMensual, min, max, bonos, \
    bruto, neto, mostrarSueldo, beneficios, nomEmpresa, empresa, pais, estado, municipio, modalidad, siguiente

def paso1():
    try:
        loginValido()
        carpeta = 'paso1'
        puestos = ['abogado', 'desarrollador', 'medico', 'contador', 'Filósofo', 'Profesor', 'Periodista', 'Enfermero']
        aleatorio = random.choice(puestos)

        click_elemento(vacantes, carpeta, 2)
        click_elemento(crearVacante, carpeta, 2)
        click_elemento(manual, carpeta, 2)
        text_elemento_intro(puesto,aleatorio,carpeta,2)
        text_elemento(especialidad,'automatizacion',carpeta,2)

        comboBox(sueldoMensual, 2, carpeta, 2)
        text_elemento(min, '20000', carpeta, 2)
        text_elemento(max, '25000', carpeta, 2)
        click_elemento(bonos, carpeta,2)
        click_elemento(bonos, carpeta,2)
        click_elemento(bonos, carpeta,2)
        scrollearElemento(bonos)

        click_elemento(bruto, carpeta,2)
        click_elemento(neto, carpeta,2)
        click_elemento(mostrarSueldo, carpeta,2)

        click_elemento(beneficios, carpeta,2)

        text_elemento_intro(nomEmpresa,'involve', carpeta, 2)
        scrollearElemento(nomEmpresa)

        comboBox(pais,1,carpeta,2)
        comboBox(estado,7,carpeta,2)
        comboBox(municipio, 10, carpeta, 2)

        comboBox(modalidad,1,carpeta,2)

        click_elemento(siguiente, carpeta,2)
        captura_time(carpeta, 2)

        print("se completo el primer paso")
        return "se cpmpleto el primer paso"
    except Exception as e:
        print("no se completo el primer paso")
        return "no se completo el primer paso"

