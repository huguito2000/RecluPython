from objetos.funciones import click_elemento, comboBox, text_elemento
from objetos.crearVacante.vacanteManual.Obj_paso4 import addPregunta, expLaboral, expPregunta, comboBox1, expSi, expNo, \
    hDura, duraPregunta, comboBox2, yearExp, hBlanda, blandaPrgunta, comboBox3, blandaSi, blamdaNo, siguiente

def p4():
    try:
        carpeta = 'paso4'
        click_elemento(addPregunta, carpeta,2)

        click_elemento(expLaboral, carpeta, 2)
        text_elemento(expPregunta, 'Hola mundo', carpeta, 2)
        comboBox(comboBox1,1, carpeta, 2)
        comboBox(comboBox1,2, carpeta, 2)
        comboBox(comboBox1,0, carpeta, 2)
        click_elemento(expSi, carpeta, 2)
        click_elemento(expNo, carpeta, 2)
        click_elemento(expSi, carpeta, 2)

        click_elemento(addPregunta, carpeta, 2)

        click_elemento(hDura, carpeta, 2)
        text_elemento(duraPregunta, 'hola mundo 2', carpeta, 2)
        comboBox(comboBox2, 1, carpeta, 2)
        comboBox(comboBox2, 2, carpeta, 2)
        text_elemento(yearExp, '2', carpeta, 2)

        click_elemento(addPregunta, carpeta, 2)

        click_elemento(hBlanda, carpeta, 2)
        text_elemento(blandaPrgunta, 'hola mundo 3', carpeta, 2)
        comboBox(comboBox3, 1, carpeta, 2)
        comboBox(comboBox3,0, carpeta, 2)
        click_elemento(blandaSi, carpeta, 2)
        click_elemento(blamdaNo, carpeta, 2)
        click_elemento(blandaSi, carpeta, 2)
        click_elemento(siguiente, carpeta, 2)
        print('paso el paso 4')
        return 'paso el paso 4'
    except Exception as e:
        print('no paso el paso 4', str(e))
        return 'no paso el paso 4'











