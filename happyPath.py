from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from test.home import pasa_home, menu, perfil, ajustes
from test.clientes import newCliente

now = datetime.now()
fecha = str(now.day) + ' del ' + str(now.month) + " en el minuto " + str(now.minute)


def generar_informe_pdf(nombre_archivo, reporteHome, reporteMenu, reportePerfil, reporteAjustes, reporteCliente):
    global fecha
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.drawString(72, 750, "Informe de Prueba")
    c.drawString(72, 720, "Fecha: " + fecha + " del 2023")

    # Agregar detalles sobre la ejecución
    c.drawString(72, 690, "Resultado de la pruebas de happy path")
    c.drawString(72, 670, reporteHome)
    c.drawString(72, 640, reporteMenu)
    c.drawString(72, 610, reportePerfil)
    c.drawString(72, 590, reporteAjustes)
    c.drawString(72, 570, reporteCliente)

    c.save()


def ReporteHappyPath():
    resultado_home = pasa_home()
    resultado_menu = menu()
    resultado_perfil = perfil()
    resultado_ajustes = ajustes()
    resultado_cliente = newCliente()
    nombre_archivo = "reportes/happyPath" + fecha + ".pdf"
    generar_informe_pdf(nombre_archivo, resultado_home, resultado_menu, resultado_perfil, resultado_ajustes,
                        resultado_cliente)

