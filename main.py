from registroCompleto import registro
from happyPath import ReporteHappyPath
from crearVacanteManual import crearVacante
from crearVacanteIA import vacanteIA
from configuracion import ajustes

if __name__ == '__main__':

    registro()
    print('termino el registro')
    ReporteHappyPath()
    print('termino el happypath')
    ajustes()
    print('se termino los ajustes')
    crearVacante()
    print('se termino la creacion de vacante')
    vacanteIA()






