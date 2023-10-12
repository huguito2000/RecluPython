from objetos.funciones import text_elemento, click_elemento, comboBox, captura_time, text_elemento_intro
from test.crearVacante.vacante_manual.paso1 import paso1
from objetos.crearVacante.vacanteManual.paso_2 import objetivo, tipoPuesto, personas_Si, personas_No, funciones, \
    jornadaLaboral, horario, contrato, guardar, siguiente

def paso2():
    try:
        paso1()
        carpeta = 'paso2'
        text_elemento(objetivo, 'hacer pruebas', carpeta, 2)
        comboBox(tipoPuesto, 7 , carpeta, 2)
        click_elemento(personas_Si, carpeta, 2)
        click_elemento(personas_No, carpeta, 2)
        text_elemento(funciones, 'hacer pruebas de funciones', carpeta, 2)
        comboBox(jornadaLaboral, 1, carpeta, 2)
        text_elemento(horario, 'todos los dias', carpeta, 2)
        comboBox(contrato, 1, carpeta, 2)
        click_elemento(siguiente, carpeta, 2)
        captura_time(carpeta, 2)
        print('Se el completo el paso 2')
        return 'Se el completo el paso 2'
    except Exception as e:
        print('no se el completo el paso 2')
        return 'no se el completo el paso 2'




