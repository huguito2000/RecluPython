import time

from objetos.Obj_home import vacantes
from test.Login import loginValido
from objetos.funciones import captura_time, click_elemento, text_elemento, comboBox
from objetos.Obj_clientes import clientes, nuevo, cerrar, nombreCliente, sector, giro, tipoEmpresa, cantidad1a10, \
    cantidad11a50, cantidad51a250, cantidad250, guardar, hambuguesa, eliminar, cancelar, eliminar2, perfil, cerrarSesion

contador: int = 0
carpeta = 'clientes'


def newCliente():
    try:
        loginValido()
        click_elemento(clientes, carpeta, 1)
        click_elemento(nuevo, carpeta, 1)
        click_elemento(cerrar, carpeta, 1)
        click_elemento(nuevo, carpeta, 1)
        text_elemento(nombreCliente, 'involver', carpeta, 1)
        comboBox(sector, 11, carpeta, 2)
        comboBox(giro, 7, carpeta, 2)
        comboBox(tipoEmpresa, 1, carpeta, 2)
        click_elemento(cantidad1a10, carpeta, 1)
        click_elemento(cantidad11a50, carpeta, 1)
        click_elemento(cantidad51a250, carpeta, 1)
        click_elemento(cantidad250, carpeta, 1)
        click_elemento(guardar, carpeta, 1)
        click_elemento(hambuguesa, carpeta, 1)
        click_elemento(eliminar, carpeta, 1)
        click_elemento(cancelar, carpeta, 1)
        click_elemento(hambuguesa, carpeta, 1)
        click_elemento(eliminar, carpeta, 1)
        click_elemento(eliminar2, carpeta, 1)
        click_elemento(vacantes, carpeta, 1)
        time.sleep(3)

        click_elemento(perfil, carpeta, 2)
        click_elemento(cerrarSesion, carpeta, 2)
        time.sleep(2)
        print("ya paso la creación y eliminación del cliente")
        return "ya paso la creación y eliminación del cliente"
    except Exception as e:
        print("falla la creacion de cliente", str(e))
        return "falla la creacion de cliente"

