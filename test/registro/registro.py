from datetime import datetime
import time
from objetos.funciones import click_elemento, text_elemento, captura_time
from objetos.registro.Obj_email import crearCuenta, email, telefono, password, mostrar1, ocultar1, password2, mostrar2, \
    ocultar2, TyC, cerrar, AvisosPrivacidad, cookies, legales, continuar

now = datetime.now()
correo = 'reclu' + str(now.day) + str(now.month) + str(now.minute) + str(now.second) + '@yopmail.com'
print(correo)
def registroPruebas():
    try:
        carpeta = 'registro'
        click_elemento(crearCuenta, carpeta, 1)
        text_elemento(email, 'reclutador', carpeta, 1)
        text_elemento(telefono, '5569777077', carpeta, 1)
        text_elemento(telefono, 'abcd.1234', carpeta, 1)
        click_elemento(mostrar1, carpeta, 1)
        click_elemento(ocultar1, carpeta, 1)
        text_elemento(password2, 'abcd.1234', carpeta, 1)
        click_elemento(mostrar2, carpeta, 1)
        click_elemento(ocultar2, carpeta, 1)
        click_elemento(TyC, carpeta, 1)
        click_elemento(cerrar, carpeta, 1)
        click_elemento(AvisosPrivacidad, carpeta, 1)
        click_elemento(cerrar, carpeta, 1)
        click_elemento(cookies, carpeta, 1)
        click_elemento(cerrar, carpeta, 1)
        click_elemento(legales, carpeta, 1)
        click_elemento(legales, carpeta, 1)
        click_elemento(continuar, carpeta, 1)
        text_elemento(email, 'reclutador', carpeta, 1)
        click_elemento(continuar, carpeta, 1)
        text_elemento(email, 'reclutador@yopmail.com', carpeta, 1)
        click_elemento(continuar, carpeta, 1)
        text_elemento(email, 'reclutadoryopmail.com', carpeta, 1)
        click_elemento(continuar, carpeta, 1)
        click_elemento(continuar, carpeta, 1)
        text_elemento(email, correo, carpeta, 1)
        text_elemento(telefono, '5569777077', carpeta, 1)
        text_elemento(password, 'Abcd.1234', carpeta, 1)
        click_elemento(mostrar1, carpeta, 1)
        click_elemento(ocultar1, carpeta, 1)
        text_elemento(password2, 'Abcd.1234', carpeta, 1)
        click_elemento(mostrar2, carpeta, 1)
        click_elemento(ocultar2, carpeta, 1)
        click_elemento(continuar, carpeta, 3)
        captura_time(carpeta, 3)
        print("ya se hizo el registro")
        return "ya se hizo el registro correctamente"
    except Exception as e:
        print("no se realizo el registro", str(e))
        return "no se realizo el registro"



def registroValido():
    try:
        global correo
        time.sleep(2)
        carpeta = 'registro'
        click_elemento(crearCuenta, carpeta, 1)
        text_elemento(email, correo, carpeta, 1)
        text_elemento(telefono, '5569777077', carpeta, 1)
        click_elemento(legales, carpeta, 1)
        text_elemento(password, 'Abcd.1234', carpeta, 1)
        click_elemento(mostrar1, carpeta, 1)
        click_elemento(ocultar1, carpeta, 1)
        text_elemento(password2, 'Abcd.1234', carpeta, 1)
        click_elemento(mostrar2, carpeta, 1)
        click_elemento(ocultar2, carpeta, 1)
        click_elemento(continuar, carpeta, 3)
        captura_time(carpeta, 3)
        print('se termino el registro valido')
        return 'se termino el registro valido correctamente'
    except Exception as e:
        print('No se termino el registro valido ', str(e))
        return 'No se termino el registro valido '



