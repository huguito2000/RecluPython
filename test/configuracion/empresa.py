from objetos.funciones import click_elemento, text_elemento, cambio_imagen, captura_time, comboBox
from objetos.Obj_home import Ajustes
from test.Login import loginValido
from test.configuracion.perfil import perfilHapyPath
from objetos.configuracion.Obj_empresa import (empresa, logo, eliminar, eliminar2, cancelar, nombreEmpresa, sector, giro,
tipoEmpresa, empleados1a10, empleados11a50, empleados50a250, empleados250, pais, cancelar2,actualizar, img_path)

def empresa():
    try:
        perfilHapyPath()
        carpeta = 'empresa'
        captura_time(carpeta,2)
        loginValido()
        captura_time(carpeta, 2)
        click_elemento(Ajustes, carpeta, 3)
        click_elemento(empresa, carpeta, 3)
        click_elemento(cancelar2, carpeta, 3)
        cambio_imagen(logo,img_path,carpeta,5)
        click_elemento(eliminar, carpeta, 2)
        click_elemento(cancelar, carpeta, 2)
        click_elemento(eliminar, carpeta, 2)
        click_elemento(eliminar2, carpeta, 2)
        cambio_imagen(logo,img_path,carpeta,5)
        text_elemento(nombreEmpresa,'involve',carpeta,1)
        comboBox(sector,11,carpeta,1)
        comboBox(giro,7,carpeta,1)
        comboBox(tipoEmpresa,1,carpeta,1)
        click_elemento(empleados1a10, carpeta, 2)
        click_elemento(empleados11a50, carpeta, 2)
        click_elemento(empleados50a250, carpeta, 2)
        click_elemento(empleados250, carpeta, 2)
        click_elemento(actualizar, carpeta, 2)
        print('ya paso la empresa')
        return 'ya paso la empresa'
    except Exception as e:
        print('no paso la empresa')
        return 'no paso la empresa'


