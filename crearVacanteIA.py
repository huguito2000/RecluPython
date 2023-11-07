from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from test.crearVacante.IA.crearVacanteIA import vacanteIA
from test.crearVacante.vacante_manual.paso1 import p1
from test.crearVacante.vacante_manual.paso2 import p2
from test.crearVacante.vacante_manual.paso3 import p3
from test.crearVacante.vacante_manual.paso4 import p4
from test.crearVacante.vacante_manual.paso5 import p5
from test.crearVacante.vacante_manual.paso6 import publicarVacante

now = datetime.now()
fecha = str(now.day) + ' del ' + str(now.month) + " en el minuto " + str(now.minute)


def generar_informe_pdf(nombre_archivo, reporteVAcanteIA):
    global fecha
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.drawString(72, 750, "Informe de Prueba")
    c.drawString(72, 720, "Fecha: " + fecha + " del 2023")

    # Agregar detalles sobre la ejecución
    c.drawString(72, 690, "Resultado de la pruebas en las funciones")
    c.drawString(72, 670, reporteVAcanteIA)
    c.save()


def VacanteIA():

    resultado_crearVacanteIA = vacanteIA()

    nombre_archivo = "reportes/CrearVancanteIA" + fecha + ".pdf"
    generar_informe_pdf(nombre_archivo, resultado_crearVacanteIA)
