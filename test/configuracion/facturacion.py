from test.configuracion.empresa import empresa
from objetos.Obj_home import Ajustes
from objetos.configuracion.Obj_facturacion import facturacion, razonSocial,rfc,regimenFiscal,CFDI,codigoPostal,recordatorios,actualizar
from objetos.funciones import text_elemento, click_elemento, comboBox, captura_time


def Testfacturacion():
    try:
        empresa()
        carpeta = 'facturacion'
        captura_time(carpeta,2)
        click_elemento(Ajustes,carpeta,1)
        click_elemento(facturacion,carpeta,1)
        text_elemento(razonSocial,'hugo rafael rodriguez olivera',carpeta,1)
        text_elemento(rfc,'ROOH881217SZ7',carpeta,1)
        comboBox(regimenFiscal,3,carpeta,2)
        comboBox(CFDI,3,carpeta,2)
        click_elemento(recordatorios,carpeta,1)
        click_elemento(actualizar,carpeta,1)
        print("se hizo la facturacion")
        return 'se hizo la facturación'
    except Exception as e:
        print('no paso la facturacion', str(e))
        return 'no se hizo la facturación'

