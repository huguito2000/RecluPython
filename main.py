from test.registro.registro import registroPruebas
from test.registro.confirmacion import registroCompleto
from test.home import pasa_home, menu, perfil, ajustes
from test.clientes import newCliente

if __name__ == '__main__':

    registroPruebas()
    registroCompleto()
    print('se termino el registro')
    pasa_home()
    menu()
    perfil()
    ajustes()
    newCliente()








