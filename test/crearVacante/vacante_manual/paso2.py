from objetos.funciones import text_elemento, click_elemento, comboBox, captura_time, text_elemento_intro
from test.crearVacante.vacante_manual.paso1 import paso1
from objetos.crearVacante.vacanteManual.Obj_paso2 import objetivo, tipoPuesto, personas_Si, personas_No, funciones, \
    jornadaLaboral, horario, contrato, guardar, siguiente

def paso2():
    try:
        paso1()
        carpeta = 'paso2'
        text_elemento(objetivo, 'hacer pruebas', carpeta, 1)
        comboBox(tipoPuesto, 7, carpeta, 1)
        click_elemento(personas_Si, carpeta, 1)
        click_elemento(personas_No, carpeta, 1)
        text_elemento(funciones, 'hacer pruebas de funciones', carpeta, 1)
        comboBox(jornadaLaboral, 1, carpeta, 1)
        text_elemento(horario, 'todos los dias', carpeta, 1)
        comboBox(contrato, 1, carpeta, 1)
        click_elemento(siguiente, carpeta, 1)
        captura_time(carpeta, 1)
        print('Se el completo el paso 2')
        return 'Se el completo el paso 2'
    except Exception as e:
        print('no se el completo el paso 2', str(e))
        return 'no se el completo el paso 2'




