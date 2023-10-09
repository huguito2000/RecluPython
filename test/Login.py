from objetos.Obj_login import email, password, BtnContinuar, mostrar, ocultar
from objetos.funciones import click_elemento, text_elemento, captura_time

def loginPrueba():
    try:
        text_elemento(email, 'hug', 'login',1)
        text_elemento(email, 'huguitoyopmail.com', 'login',1)
        text_elemento(email, 'huguito.reclutador@yopmail.com', 'login',1)

        text_elemento(password, 'abcd.1234', 'login',1)
        click_elemento(mostrar, 'login',1)
        click_elemento(ocultar, 'login',1)
        click_elemento(BtnContinuar, 'login',3)

        text_elemento(password, 'Abcd.1234', 'login',1)
        click_elemento(mostrar, 'login',1)
        click_elemento(ocultar, 'login',1)

        click_elemento(BtnContinuar, 'login',10)

        print("Inicio de sesión exitoso")
        return "Inicio de sesión exitoso"
    except Exception as e:
        print("Error al iniciar sesión:", str(e))
        return "Fallo"


def loginValido():
    try:
        text_elemento(email, 'huguito.reclutador@yopmail.com', 'login', )
        text_elemento(password, 'Abcd.1234', 'login')
        click_elemento(BtnContinuar, 'login')
        captura_time('login', 2)
        print("Inicio de sesión exitoso")
        return "Inicio de sesión exitoso"
    except Exception as e:
        print("Error al iniciar sesión:", str(e))
        return "Fallo"



