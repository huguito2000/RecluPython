from test.Login import loginValido
from objetos.browser import driver
import time
from objetos.registro.Obj_confirmacion import perfil, cerrarSesion
from objetos.funciones import click_elemento, text_elemento, cambio_imagen
from objetos.Obj_home import clientes, pausada, borrador, cerradas, activas, vacantes, Btnperfil, configuracion, nombre, \
    apaterno, amaterno, subir, img_path, creditos, equipo, historial, tutorial, chat, Ajustes, eliminar, cancelar, \
    eliminar2

carpeta = 'home'

def pasa_home():
    try:
        loginValido()
        click_elemento(pausada, carpeta, 1)
        click_elemento(borrador, carpeta, 1)
        click_elemento(cerradas, carpeta, 1)
        click_elemento(activas, carpeta, 2)
        print("paso el home")
        return ("paso el home exitosamente")
    except Exception as e:
        print("Error en el home:", str(e))
        return "Fallo el home"


def menu():
    try:
        click_elemento(creditos, carpeta, 3)
        click_elemento(vacantes, carpeta, 3)
        click_elemento(equipo, carpeta, 3)
        click_elemento(clientes, carpeta, 3)
        click_elemento(historial, carpeta, 3)
        click_elemento(chat, carpeta, 3)
        click_elemento(chat, carpeta, 3)
        click_elemento(Ajustes, carpeta, 3)
        click_elemento(tutorial, carpeta, 3)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(5)
        click_elemento(vacantes, carpeta, 3)
        print("ya regrese a la pestaña principal")
        print("paso el menu")
        return ("paso el menu exitosamente")
    except Exception as e:
        print("Error al pasar el menu", str(e))
        return "Fallo el menu"


def perfil():
    try:
        click_elemento(Btnperfil, carpeta, 1)
        click_elemento(configuracion, carpeta, 1)
        time.sleep(2)
        print("paso el perfil")
        return "paso el perfil correctamente"
    except Exception as e:
        print("Error al pasar el perfil", str(e))
        return "Fallo el perfil"


def ajustes():
    try:
        click_elemento(vacantes, carpeta, 3)
        click_elemento(Ajustes, carpeta, 3)
        text_elemento(nombre, 'huguito', carpeta, 1)
        text_elemento(apaterno, 'rodriguez', carpeta, 1)
        text_elemento(amaterno, 'olivera', carpeta, 1)
        cambio_imagen(subir, img_path, carpeta, 3)

        click_elemento(eliminar, carpeta, 3)
        click_elemento(cancelar, carpeta, 3)
        click_elemento(eliminar, carpeta, 3)
        click_elemento(eliminar2, carpeta, 3)
        cambio_imagen(subir, img_path, carpeta, 3)
        time.sleep(5)

        click_elemento(vacantes, carpeta, 3)
        click_elemento(perfil, carpeta, 2)
        click_elemento(cerrarSesion, carpeta, 2)
        time.sleep(2)

        print ("ya pasaron los ajustes")
        return "ya pasaron los ajustes correctamente"
    except Exception as e:
        print("Error al pasar los ajustes", str(e))
        return "Fallo los ajustes"



