from objetos.Obj_login import email, password, BtnContinuar, mostrar, ocultar
from objetos.funciones import click_elemento, text_elemento, captura_time

carpeta = 'login'
def loginPrueba():
    try:
        text_elemento(email, 'hug', carpeta,1)
        text_elemento(email, 'huguitoyopmail.com', carpeta,1)
        text_elemento(email, 'huguito.reclutador@yopmail.com', carpeta,1)

        text_elemento(password, 'abcd.1234', carpeta,1)
        click_elemento(mostrar, carpeta,1)
        click_elemento(ocultar, carpeta,1)
        click_elemento(BtnContinuar, carpeta,3)

        text_elemento(password, 'Abcd.1234', carpeta,1)
        click_elemento(mostrar, carpeta,1)
        click_elemento(ocultar, carpeta,1)

        click_elemento(BtnContinuar, carpeta,10)

        print("Inicio de sesión exitoso")
        return "Inicio de sesión exitoso"
    except Exception as e:
        print("Error al iniciar sesión:", str(e))
        return "Fallo"


def loginValido():
    try:
        text_elemento(email, 'huguito.reclutador@yopmail.com', carpeta, )
        text_elemento(password, 'Abcd.1234', carpeta)
        click_elemento(BtnContinuar, carpeta)
        captura_time(carpeta, 2)
        print("Inicio de sesión exitoso")
        return "Inicio de sesión exitoso"
    except Exception as e:
        print("Error al iniciar sesión:", str(e))
        return "Fallo"



