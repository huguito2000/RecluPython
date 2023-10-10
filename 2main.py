from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from test.Login import loginValido
from test.home import testSuiteHome
from test.registro import registroPruebas
from test.confirmacion import confirmacionValida
from test.clientes import newCliente
from test.configuracion.perfil import perfil
from test.configuracion.empresa import empresa

now = datetime.now()
fecha = str(now.day) + ' del ' + str(now.month)+ " en el minuto " +str(now.minute)
def generar_informe_pdf(nombre_archivo, resultado_login, resultado_home, resultado_regitroPrueba, resultado_confirmacion,
                        resultado_cliente, resultado_perfil,resultado_empresa):
    global fecha
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.drawString(72, 750, "Informe de Prueba")
    c.drawString(72, 720, "Fecha: "+ fecha + " del 2023")

    # Agregar detalles sobre la ejecución
    c.drawString(72, 690, "Resultado de la pruebas en las funciones")
    c.drawString(72, 670, resultado_login)
    '''
    c.drawString(72, 650, resultado_home)
    c.drawString(72, 530, resultado_regitroPrueba)
    c.drawString(72, 510, resultado_confirmacion)
    c.drawString(72, 490, resultado_cliente)
    c.drawString(72, 470, resultado_perfil)
    c.drawString(72, 450, resultado_empresa)
    c.save()
    '''




    '''
    resultado_login = loginValido() # Reemplaza esto con la función que obtiene los resultados de tu prueba
    resultado_home = testSuiteHome()
    resultado_menu = menu()
    resultado_perfil1 = perfil()
    resultado_ajustes = ajustes()
    resultado_registroPrueba = registroPruebas()
    resultado_confirmacion = confirmacionValida()
    resultado_cliente = newCliente()
    resultado_perfil = perfil()
    resultadoç_empresa = empresa()
    nombre_archivo = "reportes/informe"+fecha+".pdf"
    generar_informe_pdf(nombre_archivo, resultado_login, resultado_home, resultado_menu, resultado_perfil1, resultado_ajustes, resultado_registroPrueba)
    '''