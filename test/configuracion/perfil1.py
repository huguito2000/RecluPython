import time

from test.Login import loginValido
from objetos.funciones import click_elemento, text_elemento, cambio_imagen, captura_time
from objetos.configuracion.Obj_perfil import Ajustes, nombre, apaterno, amaterno, img_path, subir, eliminar, cancelar, \
    eliminar2, cambiarPass, passAnterior, newPass, confirmarPassword, cambiarPassword, mostrarPass1, mostrarPass2, \
    mostrarPass3, telefonoCambio, newTelefono, cancelarTelefono, cambiarTelefono, cambiarEmail, newEmail, newEmail2, \
    passEmail, cancelarEmail, continuarEmail, mostrarEmail, perfil, cerrarSesion

carpeta = 'perfil'
password = 'abcd.1234'


def cambioPassword():

    text_elemento(passAnterior, password, carpeta, 1)
    click_elemento(mostrarPass1, carpeta, 1)
    text_elemento(newPass, 'Abcd.1234', carpeta, 1)
    click_elemento(mostrarPass2, carpeta, 1)
    text_elemento(confirmarPassword, 'Abcd.1234', carpeta, 1)
    click_elemento(mostrarPass3, carpeta, 1)
    click_elemento(cambiarPassword, carpeta, 1)

def DatosPerfil():
    try:
        #cambio de datos personales
        global password
        loginValido()
        captura_time(carpeta, 2)
        click_elemento(Ajustes, carpeta, 3)
        text_elemento(nombre, 'huguito', carpeta, 1)
        text_elemento(apaterno, 'rodriguez', carpeta, 1)
        text_elemento(amaterno, 'olivera', carpeta, 1)

        #cambio de imagen
        cambio_imagen(subir, img_path, carpeta, 3)
        click_elemento(eliminar, carpeta, 2)
        click_elemento(cancelar, carpeta, 2)
        click_elemento(eliminar, carpeta, 2)
        click_elemento(eliminar2, carpeta, 2)
        cambio_imagen(subir, img_path, carpeta, 3)

        #cambio de contraseña
        click_elemento(cambiarPass, carpeta, 2)
        cambioPassword()
        password = 'Abcd.1234'
        cambioPassword()
        captura_time(carpeta, 2)

        loginValido()
        
        click_elemento(Ajustes, carpeta, 2)
        captura_time(carpeta, 2)
        click_elemento(Ajustes, carpeta, 2)
        click_elemento(telefonoCambio, carpeta, 2)
        click_elemento(cancelarTelefono, carpeta, 2)
        click_elemento(telefonoCambio, carpeta, 2)
        text_elemento(newTelefono, '5569777077', carpeta, 1)
        click_elemento(cambiarTelefono, carpeta, 2)

        click_elemento(cambiarEmail, carpeta, 2)
        click_elemento(cancelarEmail, carpeta, 2)
        click_elemento(cambiarEmail, carpeta, 2)
        text_elemento(newEmail, 'hugo', carpeta, 1)
        text_elemento(newEmail, 'hugoreclutador@yopmail.com', carpeta, 2)
        text_elemento(newEmail2, 'hugo', carpeta, 1)
        text_elemento(newEmail2, 'hugoreclutador@yopmail.com', carpeta, 2)

        text_elemento(passEmail, 'abcd.1234', carpeta, 1)
        click_elemento(mostrarEmail, carpeta, 2)
        click_elemento(continuarEmail, carpeta, 2)
        text_elemento(passEmail, 'Abcd.1234', carpeta, 1)
        click_elemento(continuarEmail, carpeta, 2)

        time.sleep(5)
        click_elemento(perfil, carpeta, 2)
        click_elemento(cerrarSesion, carpeta,  2)

        print("ya paso correctamente el perfil")
        return "ya paso correctamente la seccion de perfil"
    except Exception as e:
        print("no paso correctamente el perfil", str(e))
        return "no paso la seccion de perfil"



